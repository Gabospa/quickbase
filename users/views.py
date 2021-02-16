""" Users Views."""

# Django REST Framework
from rest_framework import mixins, viewsets,status
from rest_framework.decorators import action 
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

# Models
from .models import User

# Serializers
from .serializers import UserModelSerializer, UserSignUpSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ User view set for sign up """

    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self):
        """ Asign permission bassed on actions """
        if self.action in ['signup']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """ User sign up. """
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)