from rest_framework.permissions import BasePermission




from rest_framework.permissions import BasePermission

class Is_employer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.role == "employer"


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    