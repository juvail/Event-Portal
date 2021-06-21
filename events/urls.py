from django.urls import path
from . import views
urlpatterns = [
    path("",views.home , name="home"),
    path("register-event/",views.create_event,name="create_event"),
    path("user-profile/",views.profile,name="profile")
]