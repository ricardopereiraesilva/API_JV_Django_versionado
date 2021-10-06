from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_user>/', views.get_current_state, name='refresh'),
]