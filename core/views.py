from django.shortcuts import render, redirect
import time
#importamos la mensajeria de django para utilizarla
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Region, TipoVivienda, Usuario, Raza, Estado, Mascota, Genero
from .forms import FormularioMascota
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout

def logout_view(request):
    logout(request)

def home(request):
    return render(request, 'core/home.html')

def registro(request):
	usu = Usuario()
	usu2 = User()
	region = Region.objects.all()
	vivienda = TipoVivienda.objects.all()
	variables ={
		'region' : region,
		'vivienda' : vivienda
	}

	if request.POST:
        #si el request es post obtendremos las variables
        
		usu.correo = request.POST.get('txtCorreo')
		usu.clave = request.POST.get('txtClave')
		usu.rut = request.POST.get('txtRut')
		usu.nombre = request.POST.get('txtNombre')
		usu.apellido = request.POST.get('txtApellido')
		usu.fecha_nacimiento = request.POST.get('txtFechaNacimiento')
		usu.telefono = request.POST.get('txtTelefono')
		#crearemos un objeto Region para obtener el id de la region
		region = Region()
		region.id = request.POST.get('cboRegion')
        #guardamos region dentro de region
		usu.region = region
		tipoVivienda = TipoVivienda()
		tipoVivienda.id = request.POST.get('cboVivienda')
        #guardamos tipoVivienda dentro de tipoVivienda
		usu.tipoVivienda = tipoVivienda
		
		usu2.password = usu.clave
		usu2.is_superuser = 0
		usu2.username = usu.correo
		usu2.first_name = usu.nombre
		usu2.email = usu.correo
		usu2.is_staff = 0
		usu2.is_active = 1
		usu2.date_joined = '2018-11-29'
		usu2.last_name = usu.apellido

		usu.save()
        #procederemos a guardar al auto en la BBDD
		try:
			usu2.set_password(usu2.password)
			usu2.save()
			usu2.set_password(usu2.password)
			variables['mensaje'] = 'Guardado correctamente'
		except:
			variables['mensaje'] = 'No se ha podido guardar'
	return render(request, 'core/registro.html', variables)

	
def listarMascotas(request):
    m=Mascota.objects.all()
    return render(request,'core/listarMascotas.html',{'Mascota':m})

def eliminarMascota(request,id):
    mas = Mascota.objects.get(id=id)
    try:
        mas.delete()
        mensaje = "La mascota se ha eliminado con exito"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar la mascota"
        messages.error(request , mensaje)
    return redirect('listarMascotas')




def registroMascotas(request):
	raza = Raza.objects.all()
	genero = Genero.objects.all()
	estado = Estado.objects.all()
	variables ={
		'raza' : raza,
		'genero' : genero,
		'estado' : estado,
	}
	if request.POST:
		perri=Mascota()
		perri.nombreMascota = request.POST.get('txtNombre2')
		perri.fecha_ingreso = request.POST.get('fecha_ingresoMascota')
		perri.fecha_nacimientoMascota = request.POST.get('fecha_nacimientoMascota')
		raza = Raza()
		raza.id = request.POST.get('cboRaza')
		perri.raza = raza
		try:
			perri.save()
			variables['mensaje']='Guardado correctamente'
		except:
			variables['mensaje']='No se ha podido guardar'  
	return render(request, 'core/registroMascotas.html', variables)


def modificarMascotas(request, id):

    mascota = Mascota.objects.get(id=id)

    raza = Raza.objects.all()
    genero = Genero.objects.all()
    estado = Estado.objects.all()

    #buscamos el automovil en la BBDD por su ID
    variables = {
        'mascota':mascota,
        'raza':raza,
        'genero': genero,
        'estado': estado
    }

    if request.POST:
        mascota = Mascota()

        mascota.id = request.POST.get('idmascota')

        mascota.nombre = request.POST.get('nombreMascota')

        raza = Raza()
        raza.id = request.POST.get('raza')
        mascota.raza = raza

        genero = Genero()
        genero.id = request.POST.get('genero')
        mascota.genero = genero 

        mascota.fechaNacimiento = request.POST.get('fecha_nacimientoMascota')
        
        mascota.fechaIngreso = request.POST.get('id_fecha_ingreso')

        mascota.imagen = request.FILES.get('imagenbox')        

        estado = Estado()
        estado.id = request.POST.get('estado')
        mascota.estado = estado      

        #actualizar
        try:
            mascota.save()
            messages.success(request, "Modificado correctamente")
        except:
            messages.error(request, "No se ha podido actualizar")

        #redirect al listar
        return redirect('listarMascotas')

    return render(request, 'core/ModificarMascotas.html', variables)
 

def login(request):
    us=Usuario.objects.all()
    #----
    if request.POST:
        usu=request.POST.get("username")
        passwd=request.POST.get("password",)
        user=auth.authenticate(username=usu,password=passwd)
        if user is not None and user.is_active:
            if user.is_staff :
                auth.login(request,user)
                return render(request,'core/home.html',{'ingresado':True,'admin':True})
            else:
                auth.login(request,user)
                return render(request,'core/home.html',{'ingresado':True,'usuario':user.username})
        
        else:
            return render(request,'core/login.html',{'error':True})
    else:
        return render(request,'core/login.html')
