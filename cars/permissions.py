from rest_framework import permissions


class CarOwnerPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if view.action == 'list':
            view.queryset = view.queryset.filter(owner = request.user)#Verifica se o proprietário é igual ao usuário logado e tem permissão para praticar alguma ação sobre essa lista de veículos.
            return True
        return super().has_permission(request, view)#Permissão padrão
    
    def has_object_permisson(self, request, view, obj):
        return obj.owner == request.user#Verifica se o usuário é proprietário do veiculo e tem permissão para praticar alguma ação sobre o objeto