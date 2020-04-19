from django.urls import path
from user_info import views

urlpatterns = [
    path('',views.show_user_info,name='user-info'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('signup/',views.user_signup,name='signup'),
    path('<bus_name>' , views.show_bus_info, name = 'bus-name'),

    #path('bus/found',views.show_user_info,name='user-info')

]
