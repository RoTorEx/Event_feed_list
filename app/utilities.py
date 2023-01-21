from typing import Any

from .models import Advertising
from .serializers import AdvertisingSerializer


def get_advertising() -> Any:
    """Get all advertisements from request."""

    advertising_list = Advertising.objects.all().order_by("-date_create")
    return AdvertisingSerializer(advertising_list, many=True).data
