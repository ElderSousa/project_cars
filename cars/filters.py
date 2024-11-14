from dj_rql.filter_cls import AutoRQLFilterClass
from cars.models import Brand, Car


class BrandFilterClass(AutoRQLFilterClass):#Criará filtros automáticos na model Brand

    MODEL = Brand


class CarFilterClass(AutoRQLFilterClass):
    
    MODEL = Car
    FILTERS = [
        {
            'filter': 'brand',
            'source': 'brand__name',#Vai filtrar usando o nome ligado ao Id da tabela brand ex:?eq(brand,Fiat)
        },
        {
            'filter': 'owner',
            'source': 'owner__username'#Vai buscar pelo nome do usuário na tabela usuário
        }
    ]