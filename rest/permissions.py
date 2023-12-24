from rest_framework import permissions


class IsPaidUserPermission(permissions.BasePermission):
    message = 'You don\'t have permission to access this resource.'

    def has_permission(self, request, view):
        if view.action == 'paid_books':
            return request.user.is_paid
        return True


class IsAdminUpdatePermission(permissions.BasePermission):
    message = 'You don\'t have permission to access this resource.'

    def has_permission(self, request, view):
        if view.action == 'update' or view.action == 'partial_update':
            return request.user.is_staff
        return True