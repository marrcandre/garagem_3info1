from rest_framework.viewsets import ModelViewSet

from core.models import Acessorio
from core.serializers import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
