from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path("", views.inicio, name="inicio"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # Estudiantes
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("estudiantes/agregar/", views.agregar_estudiante, name="agregar_estudiante"),
    path("estudiantes/editar/<int:id>/", views.editar_estudiante, name="editar_estudiante"),
    path("estudiantes/eliminar/<int:id>/", views.eliminar_estudiante, name="eliminar_estudiante"),

    # Docentes
    path("docentes/", views.docentes, name="docentes"),
    path("docentes/agregar/", views.agregar_docente, name="agregar_docente"),
    path("docentes/editar/<int:id>/", views.editar_docente, name="editar_docente"),
    path("docentes/eliminar/<int:id>/", views.eliminar_docente, name="eliminar_docente"),

    # Faltas
    path("faltas/", views.faltas, name="faltas"),
    path("faltas/agregar/", views.agregar_falta, name="agregar_falta"),
    path("faltas/editar/<int:id>/", views.editar_falta, name="editar_falta"),
    path("faltas/eliminar/<int:id>/", views.eliminar_falta, name="eliminar_falta"),
    path("faltas/pendientes/", views.faltas_pendientes, name="faltas_pendientes"),
    path("faltas/revisar/<int:id>/",views.revisar_falta, name="revisar_falta"),
    path("estudiantes/historial/<int:id>/", views.historial_estudiante, name="historial_estudiante"),
    path("estadisticas/", views.estadisticas, name="estadisticas"),
    path("faltas/justificar/<int:id>/",views.justificar_falta, name="justificar_falta"),
]