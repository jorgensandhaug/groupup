from rest_framework import permissions


class UserAccessToMatchPermission(permissions.BasePermission):
    message = "You are not allowed to access this match"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            obj.group1.members.filter(id=request.user.id).exists()
            or obj.group2.members.filter(id=request.user.id).exists()
        )


class UserAdminForGroupPermission(permissions.BasePermission):
    message = "You are not the groupadmin for this group"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.groupAdmin == request.user
