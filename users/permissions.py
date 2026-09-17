from rest_framework.permissions import BasePermission




class Is_job_seeker(BasePermission):
    def has_permission(self, request, view):
        return ( 
            request.user.is_authenticated
            and request.user.profile.role=="candidate"
        )

class isOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user



