
from rest_framework import viewsets
from cars.models import Brand, Car
from cars.serializer import BrandSerializer, CarSerializer
from dj_rql.drf import RQLFilterBackend
from cars.filters import BrandFilterClass, CarFilterClass
from cars.permissions import CarOwnerPermission, permissions


class BrandModelVeiwSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [RQLFilterBackend] #Informa que os filtros da view serão RQL
    rql_filter_class = BrandFilterClass #Class onde serão criados os filtros


class CarModelViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CarFilterClass
    permission_classes = [permissions.DjangoModelPermissions, CarOwnerPermission, ]#Verifica as permissões por ordem respeitando a hierarquia
