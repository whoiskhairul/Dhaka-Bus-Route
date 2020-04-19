from django.contrib import admin
from django.urls import path,include
from user_info import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bus/',include('user_info.urls'),name='user'),
    path('map/',include('map.urls'),name='map'),
    path('',views.show_user_info)

]
