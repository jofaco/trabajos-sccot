from django.urls import path
from . import views

app_name = 'BibliotecaEposters'
urlpatterns = [
    # user
    path('list', views.getList, name='biblioteca_eposters_list'),
    path('list/<str:capitulo>', views.getListCapitulo, name='biblioteca_eposters_list'),
    #path('edit_User/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    #path('delete_user/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]