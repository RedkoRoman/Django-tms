from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from authentication.models import CustomUser
from authentication.serializers import UserSerializer, UserUpdateSerializer


class CustomUserViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    serializer_classes = {
        'update': UserUpdateSerializer,
        'partial_update': UserUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


# api/auth/users/ - list, create
# api/auth/users/me/ - retrieve