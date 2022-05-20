"""Serializers of providers application for json parsing"""
from providers.models import Charge, Provider, SubscriptionType
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    """provider model serializer in providers application"""

    logo_url = serializers.URLField(source="logo_key")

    class Meta:
        """Meatadata for ProviderSerializer"""

        model = Provider
        fields = ["id", "tmdb_id", "name", "link", "logo_url"]
        read_only_fields = ["__all__"]


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    """SubscriptionType model serializer for json parsing"""

    class Meta:
        """Metadata of SubscriptionTypeSerializer"""

        model = SubscriptionType
        fields = "__all__"


class ChargeSerializer(serializers.ModelSerializer):
    """Charge model serializer in providers application"""

    provider = serializers.SerializerMethodField()
    subscriptionType = serializers.SerializerMethodField()

    class Meta:
        """Meatadata for ChargeSerializer"""

        model = Charge
        fields = "__all__"

    def get_provider(self, obj):
        """Get proivder data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_subscription_type(self, obj):
        """Get subscription type data using SubscriptionTypeSerializer"""
        return SubscriptionTypeSerializer(obj.subscription_type).data


class ProviderListSerializer(serializers.ModelSerializer):
    """provider model serializer in providers application"""

    logo_url = serializers.URLField(source="logo_key")

    class Meta:
        """Meatadata for ProviderSerializer"""

        model = Provider
        fields = ["name", "logo_url"]
