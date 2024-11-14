from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import BrandModelVeiwSet, CarModelViewSet


router =DefaultRouter()
router.register('brands', BrandModelVeiwSet)
router.register('cars', CarModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]