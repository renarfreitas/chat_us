from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<pk>', views.RoomDatailView.as_view(), name="index")
]