from django.urls import path
from .views import signup, auth_page, login_view, logout_view, cadastro_sucesso

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('auth/', auth_page, name='auth_page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('cadastro/sucesso/', cadastro_sucesso, name='cadastro_sucesso'),

]
