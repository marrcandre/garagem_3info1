from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.order_by("modelo")
    serializer_class = VeiculoSerializer
