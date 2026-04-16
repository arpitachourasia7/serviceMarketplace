from rest_framework.permissions import BasePermission

class IsProvider(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'provider'
    
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'customer'
    