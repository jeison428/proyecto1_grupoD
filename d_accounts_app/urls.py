from django.urls import path, include
from knox import views as knox_views
from .api import UserAPI, LoginAPI, CreateUserAPI, ConsultUser_PersonalAPI, ConsultUserAPI

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/create_user', CreateUserAPI.as_view()),
    #path('api/auth/create_user2', CreateUserAPI2.as_view()),
    path('api/auth/consult_user', ConsultUserAPI.as_view()),
    path('api/auth/consult_user/<int:id>', ConsultUser_PersonalAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    #path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
    # INCLUIR REST API PARA LOGIN Y VERIFICACION DE TOKEN
    # VER EJ. EN EL SIGUIENTE LINK: https://github.com/kabutoblanco/jacobo_panaderia/tree/master/app_accounts
]