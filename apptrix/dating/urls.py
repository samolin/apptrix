from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static




#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)



urlpatterns = [
    #path('', include(router.urls)),
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/', views.UserListView.as_view()),
    path('create/', views.UserCreateView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)