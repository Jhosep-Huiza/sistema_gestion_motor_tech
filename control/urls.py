from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("registro/", views.registro, name="registro"),
    path("reportes/", views.reportes, name="reportes"),
    path("<str:entidad>/", views.listado, name="listado"),
    path("<str:entidad>/nuevo/", views.crear, name="crear"),
    path("<str:entidad>/<int:pk>/editar/", views.editar, name="editar"),
    path("<str:entidad>/<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]
