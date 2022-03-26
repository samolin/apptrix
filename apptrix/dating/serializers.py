from rest_framework import serializers

from .models import User


from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('image',)
        #fields = '__all__'


class ImageViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(img=self.request.data.get('img'))