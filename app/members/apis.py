from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()


class UserListAPIView(generics.ListAPIView):
    """
    회원가입한 모든 유저 목록 불러오기
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SpecificUserAPIView(APIView):
    """
    회원가입한 유저 중에서 한 명 정보만 불러오기
    """
    # DjangoModelPermissionsOrAnonReadOnly 에러 때문에 추가함
    # https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions
    queryset = User.objects.none()

    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
