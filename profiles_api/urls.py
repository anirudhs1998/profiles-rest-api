from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name = 'hello-viewset')
router.register('profile',views.UserProfileViewSet) #basename only for viewset without query set or override name of query set

urlpatterns =  [
    path('hello-view/',views.HelloAPIView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))  #register = generates a list of urls associated with our viewset and the functions inside it
    #we dont put any prefix to the url in the path. So leave it as ''
]
