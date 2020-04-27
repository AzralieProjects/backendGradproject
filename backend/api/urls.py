
# from django.contrib import admin
# from django.urls import path
# from rest_framework import routers
# from django.conf.urls import include
# from .import views
# router=routers.DefaultRouter()
# router.register('api_convert',views.api_convert)
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('', views.api_convert,name='api_convert'),

# ]

# urlpatterns = [
#      path('', views.api_convert, name='api_convert'),
#       ]

from django.urls import path
from rest_framework import routers
from django.conf.urls import include
# from .views import MovieViewSet, RatingViewSet, UserViewSet
from .views import My_TestViewSet

router = routers.DefaultRouter()
router.register(r'My_Test', My_TestViewSet,basename='My_Test')
# router.register('movies', MovieViewSet)
# router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]