from django.shortcuts import render, redirect
from .models import Estudiante, Docente


def inicio(request):
    return render(request, "core/inicio.html")


def login(request):
    return render(request, "core/login.html")


def dashboard(request):
    return render(request, "core/dashboard.html")


def estudiantes(request):
    lista = Estudiante.objects.all()

    return render(request, "core/estudiantes.html", {
        "estudiantes": lista
    })


def agregar_estudiante(request):

    if request.method == "POST":

        Estudiante.objects.create(
            documento=request.POST["documento"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            curso=request.POST["curso"]
        )

        return redirect("estudiantes")

    return render(request, "core/agregar_estudiante.html")

def editar_estudiante(request, id):

    estudiante = Estudiante.objects.get(id=id)

    if request.method == "POST":
        estudiante.documento = request.POST["documento"]
        estudiante.nombre = request.POST["nombre"]
        estudiante.apellido = request.POST["apellido"]
        estudiante.curso = request.POST["curso"]
        estudiante.save()

        return redirect("estudiantes")

    return render(request, "core/editar_estudiante.html", {
        "estudiante": estudiante
    })


def eliminar_estudiante(request, id):

    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()

    return redirect("estudiantes") 

def docentes(request):
    lista = Docente.objects.all()

    return render(request, "core/docentes.html", {
        "docentes": lista
    })
def agregar_docente(request):

    if request.method == "POST":

        Docente.objects.create(
            documento=request.POST["documento"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"]
        )

        return redirect("docentes")

    return render(request, "core/agregar_docente.html")  
def editar_docente(request, id):

    docente = Docente.objects.get(id=id)

    if request.method == "POST":
        docente.documento = request.POST["documento"]
        docente.nombre = request.POST["nombre"]
        docente.apellido = request.POST["apellido"]
        docente.save()

        return redirect("docentes")

    return render(request, "core/editar_docente.html", {
        "docente": docente
    })


def eliminar_docente(request, id):

    docente = Docente.objects.get(id=id)
    docente.delete()

    return redirect("docentes") 

from .models import Falta, Estudiante, Docente


def faltas(request):
    lista = Falta.objects.all()

    return render(request, "core/faltas.html", {
        "faltas": lista
    })


def agregar_falta(request):

    if request.method == "POST":

        tipo = request.POST["tipo"]

        if tipo == "dia":
            materia = ""
            hora = ""
        else:
            materia = request.POST["materia"]
            hora = request.POST["hora"]

        Falta.objects.create(
            estudiante=Estudiante.objects.get(id=request.POST["estudiante"]),
            docente=Docente.objects.get(id=request.POST["docente"]),
            fecha=request.POST["fecha"],
            tipo=tipo,
            materia=materia,
            hora=hora,
            estado="Pendiente"
        )

        return redirect("faltas")

    return render(request, "core/agregar_falta.html", {
        "estudiantes": Estudiante.objects.all(),
        "docentes": Docente.objects.all()
    })

def editar_falta(request, id):

    falta = Falta.objects.get(id=id)

    if request.method == "POST":

        falta.estudiante = Estudiante.objects.get(id=request.POST["estudiante"])
        falta.docente = Docente.objects.get(id=request.POST["docente"])
        falta.fecha = request.POST["fecha"]

        tipo = request.POST["tipo"]
        falta.tipo = tipo

        if tipo == "dia":
            falta.materia = ""
            falta.hora = ""
        else:
            falta.materia = request.POST["materia"]
            falta.hora = request.POST["hora"]

        falta.motivo = request.POST["motivo"]
        falta.justificada = "justificada" in request.POST

        falta.save()

        return redirect("faltas")

    return render(request, "core/editar_falta.html", {
        "falta": falta,
        "estudiantes": Estudiante.objects.all(),
        "docentes": Docente.objects.all()
    })


def eliminar_falta(request, id):

    falta = Falta.objects.get(id=id)
    falta.delete()

    return redirect("faltas")
    
    
def editar_falta(request, id):

    falta = Falta.objects.get(id=id)

    if request.method == "POST":

        tipo = request.POST["tipo"]

        if tipo == "dia":
            materia = ""
            hora = ""
        else:
            materia = request.POST["materia"]
            hora = request.POST["hora"]

        falta.estudiante = Estudiante.objects.get(id=request.POST["estudiante"])
        falta.docente = Docente.objects.get(id=request.POST["docente"])
        falta.fecha = request.POST["fecha"]
        falta.tipo = tipo
        falta.materia = materia
        falta.hora = hora
        falta.motivo = request.POST["motivo"]
        falta.estado = request.POST["estado"]

        falta.save()

        return redirect("faltas")

    return render(request, "core/editar_falta.html", {
        "falta": falta,
        "estudiantes": Estudiante.objects.all(),
        "docentes": Docente.objects.all()
    })

def historial_estudiante(request, id):

    estudiante = Estudiante.objects.get(id=id)

    faltas = Falta.objects.filter(estudiante=estudiante).order_by("-fecha")

    origen = request.GET.get("origen", "estudiantes")

    return render(request, "core/historial_estudiante.html", {
        "estudiante": estudiante,
        "faltas": faltas,
        "origen": origen
    })

from django.db.models import Count

def estadisticas(request):

    total_faltas = Falta.objects.count()

    pendientes = Falta.objects.filter(
        estado="Pendiente"
    ).count()

    aprobadas = Falta.objects.filter(
        estado="Aprobada"
    ).count()

    rechazadas = Falta.objects.filter(
        estado="Rechazada"
    ).count()

    estudiante_mas_faltas = (
        Estudiante.objects.annotate(
            total=Count("falta")
        )
        .order_by("-total")
        .first()
    )

    return render(request, "core/estadisticas.html", {

        "total_faltas": total_faltas,

        "pendientes": pendientes,

        "aprobadas": aprobadas,

        "rechazadas": rechazadas,

        "estudiante_mas_faltas": estudiante_mas_faltas

    })

def faltas_pendientes(request):

    pendientes = Falta.objects.filter(
        estado="Pendiente"
    ).order_by("-fecha")

    return render(request, "core/faltas_pendientes.html", {
        "pendientes": pendientes
    })

def revisar_falta(request, id):

    falta = Falta.objects.get(id=id)

    if request.method == "POST":

        accion = request.POST["accion"]

        if accion == "aprobar":
            falta.estado = "Aprobada"

        elif accion == "rechazar":
            falta.estado = "Rechazada"

        falta.save()

        return redirect("faltas_pendientes")

    return render(request, "core/revisar_falta.html", {
        "falta": falta
    })

def justificar_falta(request, id):

    falta = Falta.objects.get(id=id)

    if request.method == "POST":

        falta.fecha_justificacion = request.POST["fecha_justificacion"]
        falta.observaciones = request.POST["observaciones"]

        if "documento" in request.FILES:
            falta.documento = request.FILES["documento"]

        falta.save()

        return redirect("historial_estudiante", falta.estudiante.id)

    return render(request, "core/justificar_falta.html", {
        "falta": falta
        
    })