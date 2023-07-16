from rest_framework import permissions

class ItemCreationPermission(permissions.BasePermission):
    '''this is used to allow only super users can add the data of items '''
    def has_permission(self, request,view):
        if request.method == 'GET':
            return True
        return request.user.is_superuser
            