from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django_filters import rest_framework as filters




from .serializers import UserListSerializer
from .models import User


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('sex', 'name', 'surname',)

   # def get(self, request):
   #     users = User.objects.all().order_by('name')
   #     serializer = UserListSerializer(users, many=True)
   #     return Response(serializer.data)


class UserCreateView(generics.CreateAPIView):
        serializer_class = UserListSerializer