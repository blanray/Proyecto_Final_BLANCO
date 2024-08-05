from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_user, name = 'register'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('update/', views.update_user, name = 'update'),
    path('updateAvatar/', views.update_avatar, name = 'updateAvatar'),
    path('passUpdate/', views.PassUpdate.as_view(), name = 'updatePass'),
]
