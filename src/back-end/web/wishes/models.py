"""Wishes App Model Definitions: Wish"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from videos.models import Video


class Wish(models.Model):
    """Wish information that user wants to watch"""

    id = models.BigAutoField(
        primary_key=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        Video,
        null=False,
        on_delete=models.CASCADE,
    )
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        """Metadata for wish model"""

        db_table = "wish"

    def __str__(self):
        return f"{self.user}님이 {self.video} 작품을 찜하였습니다."
