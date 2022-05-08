"""Video Api"""

from django.core.exceptions import FieldError
from django.core.paginator import Paginator  # 페이징 용도
from djongo.models import Q
from providers.models import Provider
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from video_providers.models import VideoProvider
from videos.models import Video


class CustomHomeException(APIException):
    """custom Exception For HomeView"""

    status_code = 400
    default_detail = "올바르지 않은 형식입니다."
    default_code = "Bad Request Key"


class CustomSearchException(APIException):
    """custom Search Exception for homeView"""

    status_code = 404
    default_detail = "존재하지 않은 결과값입니다."
    default_code = "None Result"


class HomeView(viewsets.ViewSet):
    """Home 화면에서 video 목록을 보여주는 역할"""

    sort_dict = {
        "random": "id",
        "new": "offer_date",
        "release": "release_date",
        "dib": "dibs_count",
        "star": "star_count",
        "rating": "rating",
    }

    def search(self, key):
        """search 기능 대행"""
        try:
            queryset = Video.objects.filter(Q(title__icontains=key))
            return queryset
        except FieldError as e:
            raise CustomHomeException() from e

    def filter_provider(self, key):
        """provider의 filtering 기능 대행"""
        subqueryset = VideoProvider.objects.filter(Q(provider=None))

        try:
            for item in key:
                provider_obj = Provider.objects.get(Q(name=item))
                subqueryset = subqueryset | provider_obj.videoprovider_set.all()
        except Provider.DoesNotExist as e:
            raise CustomHomeException() from e

        video_list = Video.objects.filter(Q(id=None))
        for item in subqueryset.values("video"):
            video_list = video_list | Video.objects.filter(Q(id=item["video"]))

        return video_list

    def list(self, request):
        """Get method 적용시 사용"""

        search_target = self.request.query_params.get("search", default="")
        queryset = self.search(search_target)

        # 필터링 조건, 조건 안에서는 or처리, 조건 밖에서는 And 처리로 필터링한다.
        providers = self.request.query_params.get("providers", None)
        categories = self.request.query_params.get("categories", None)

        try:
            if categories is not None:
                queryset = queryset.filter(Q(category=categories))
        except FieldError as e:
            raise CustomHomeException() from e

        if (providers is not None) & ("," in providers):
            providers = providers.split(",")
        elif providers is not None:
            providers = providers.split()
        else:
            providers = []

        query_provider = self.filter_provider(providers)
        queryset = queryset & query_provider

        sort = self.request.query_params.get("sort", default="random")
        try:
            queryset = queryset.order_by(self.sort_dict[sort])
        except FieldError as e:
            raise CustomHomeException() from e

        page = self.request.GET.get("page", default=1)
        size = self.request.GET.get("size", default=25)
        paginator = Paginator(queryset, size)
        page_obj = paginator.get_page(page)

        data_lists = []
        for model in page_obj.object_list:
            provider_list = []
            query = VideoProvider.objects.filter(Q(video=model))
            for video in query:
                provider_name = video.provider.all().values("name")[0]["name"]
                provider_list.append(provider_name)
            temp = {
                "title": model.title,
                "title_english": model.title_english,
                "poster_key": model.poster_key,
                "film_rating": model.film_rating,
                "release_date": model.release_date.year,
                "category": model.category,
                "providers": provider_list,
            }
            data_lists.append(temp)

        context = {
            "result": data_lists,
            "page": {
                "current": page,
                "total_page": paginator.num_pages,
                "total_result": paginator.count,
            },
        }

        return Response(context)
