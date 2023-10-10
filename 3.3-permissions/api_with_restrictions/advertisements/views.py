from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework

from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.filters import AdvertisementFilter
from advertisements.serializers import AdvertisementSerializer
from advertisements.permission import IsOwner


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    """ViewSet для объявлений."""
    permission_classes = [IsOwner, IsAuthenticated]
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwner()]
        return []
