from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_staff


class IsHairdresserOrClient(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.hairdresser.id == request.user.id or obj.client == request.user
