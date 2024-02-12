from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import MotoForm, UserRegisterForm, UserEditForm, CustomAuthenticationForm
from .models import motos, Comentario
from django.contrib.auth.decorators import login_required
from PIL import Image

# Create your views here.
def home(request):
    moto = motos.objects.all()
    return render(request, 'home.html', {
        'moto': moto
    })

def honda(request):
    moto = motos.objects.filter(marca='honda')
    return render(request, 'honda.html', {
        'moto': moto
    })

@login_required
def honda_detalle(request, id):
    moto = get_object_or_404(motos, pk=id)
    comentario = Comentario.objects.filter(motos_id=id).values('id', 'descripcion', 'nombre')
    return render(request, 'hondaDetalle.html', {
        'moto': moto,
        'comentario': comentario
    })

@login_required
def honda_edicion(request, id):
    if request.method == 'GET':
        moto = get_object_or_404(motos, pk=id, usuario=request.user)
        form = MotoForm(instance=moto)
        return render(request, "hondaEdicion.html", {
            'form': form
        })
    else:
        try:
            moto = get_object_or_404(motos, pk=id, usuario=request.user)
            if len(request.FILES) == 0:
                form = MotoForm(request.POST,instance=moto)
                form.save()
            else:         
                moto.imagen = 'Imagenes/' + request.FILES['imagen'].name
                moto.save()
                form = MotoForm(request.POST,instance=moto)
                form.save()
                carpeta_imagen = "BLOG/STATIC/IMAGENES/"
                nombre_imagen = request.FILES["imagen"].name
                img = Image.open(request.FILES["imagen"])
                img.save(carpeta_imagen + nombre_imagen)

            return redirect('hondaDetalle', id=id)
        except ValueError:
            return render(request, "hondaEdicion.html", {
                'form': form,
                'error': 'Error en la actualizacion'
            })

@login_required
def honda_eliminar(request, id):
    moto = get_object_or_404(motos, pk=id, usuario=request.user)
    moto.delete()
    return redirect('honda')
    

def bajaj(request):
    moto = motos.objects.filter(marca='bajaj')
    return render(request, 'bajaj.html', {
        'moto': moto
    })

@login_required
def bajaj_detalle(request, id):
    moto = get_object_or_404(motos, pk=id)
    comentario = Comentario.objects.filter(motos_id=id).values('id', 'descripcion', 'nombre')
    return render(request, 'bajajDetalle.html', {
        'moto': moto,
        'comentario': comentario
    })

@login_required
def bajaj_edicion(request, id):
    if request.method == 'GET':
        moto = get_object_or_404(motos, pk=id, usuario=request.user)
        form = MotoForm(instance=moto)
        return render(request, "bajajEdicion.html", {
            'form': form
        })
    else:
        try:
            moto = get_object_or_404(motos, pk=id, usuario=request.user)
            if len(request.FILES) == 0:
                form = MotoForm(request.POST,instance=moto)
                form.save()
            else:         
                moto.imagen = 'Imagenes/' + request.FILES['imagen'].name
                moto.save()
                form = MotoForm(request.POST,instance=moto)
                form.save()
                carpeta_imagen = "BLOG/STATIC/IMAGENES/"
                nombre_imagen = request.FILES["imagen"].name
                img = Image.open(request.FILES["imagen"])
                img.save(carpeta_imagen + nombre_imagen)
                
            return redirect('bajajDetalle', id=id)
        except ValueError:
            return render(request, "bajajEdicion.html", {
                'form': form,
                'error': 'Error en la actualizacion'
            })
        
@login_required
def bajaj_eliminar(request, id):
    moto = get_object_or_404(motos, pk=id, usuario=request.user)
    moto.delete()
    return redirect('bajaj')        

def yamaha(request):
    moto = motos.objects.filter(marca='yamaha')
    return render(request, 'yamaha.html', {
        'moto': moto
    })

@login_required
def yamaha_detalle(request, id):
    moto = get_object_or_404(motos, pk=id)
    comentario = Comentario.objects.filter(motos_id=id).values('id', 'descripcion', 'nombre')
    return render(request, 'yamahaDetalle.html', {
        'moto': moto,
        'comentario': comentario
    })

@login_required
def yamaha_edicion(request, id):
    if request.method == 'GET':
        moto = get_object_or_404(motos, pk=id, usuario=request.user)
        form = MotoForm(instance=moto)
        return render(request, "yamahaEdicion.html", {
            'form': form
        })
    else:
        try:
            moto = get_object_or_404(motos, pk=id, usuario=request.user)
            if len(request.FILES) == 0:
                form = MotoForm(request.POST,instance=moto)
                form.save()
            else:         
                moto.imagen = 'Imagenes/' + request.FILES['imagen'].name
                moto.save()
                form = MotoForm(request.POST,instance=moto)
                form.save()
                carpeta_imagen = "BLOG/STATIC/IMAGENES/"
                nombre_imagen = request.FILES["imagen"].name
                img = Image.open(request.FILES["imagen"])
                img.save(carpeta_imagen + nombre_imagen)
                
            return redirect('yamahaDetalle', id=id)
        except ValueError:
            return render(request, "yamahaEdicion.html", {
                'form': form,
                'error': 'Error en la actualizacion'
            })
        
@login_required
def yamaha_eliminar(request, id):
    moto = get_object_or_404(motos, pk=id, usuario=request.user)
    moto.delete()
    return redirect('yamaha')   

def ktm(request):
    moto = motos.objects.filter(marca='ktm')
    return render(request, 'ktm.html', {
        'moto': moto
    })

@login_required
def ktm_detalle(request, id):
    moto = get_object_or_404(motos, pk=id)
    comentario = Comentario.objects.filter(motos_id=id).values('id', 'descripcion', 'nombre')
    return render(request, 'ktmDetalle.html', {
        'moto': moto,
        'comentario': comentario
    })

@login_required
def ktm_edicion(request, id):
    if request.method == 'GET':
        moto = get_object_or_404(motos, pk=id, usuario=request.user)
        form = MotoForm(instance=moto)
        return render(request, "ktmEdicion.html", {
            'form': form
        })
    else:
        try:
            moto = get_object_or_404(motos, pk=id, usuario=request.user)
            if len(request.FILES) == 0:
                form = MotoForm(request.POST,instance=moto)
                form.save()
            else:         
                moto.imagen = 'Imagenes/' + request.FILES['imagen'].name
                moto.save()
                form = MotoForm(request.POST,instance=moto)
                form.save()
                carpeta_imagen = "BLOG/STATIC/IMAGENES/"
                nombre_imagen = request.FILES["imagen"].name
                img = Image.open(request.FILES["imagen"])
                img.save(carpeta_imagen + nombre_imagen)
                
            return redirect('ktmDetalle', id=id)
        except ValueError:
            return render(request, "ktmEdicion.html", {
                'form': form,
                'error': 'Error en la actualizacion'
            })
        
@login_required
def ktm_eliminar(request, id):
    moto = get_object_or_404(motos, pk=id, usuario=request.user)
    moto.delete()
    return redirect('ktm')   

def bmw(request):
    moto = motos.objects.filter(marca='bmw')
    return render(request, 'bmw.html', {
        'moto': moto
    })

@login_required
def bmw_detalle(request, id):
    moto = get_object_or_404(motos, pk=id)
    comentario = Comentario.objects.filter(motos_id=id).values('id', 'descripcion', 'nombre')
    return render(request, 'bmwDetalle.html', {
        'moto': moto,
        'comentario': comentario
    })

@login_required
def bmw_edicion(request, id):
    if request.method == 'GET':
        moto = get_object_or_404(motos, pk=id, usuario=request.user)
        form = MotoForm(instance=moto)
        return render(request, "bmwEdicion.html", {
            'form': form
        })
    else:
        try:
            moto = get_object_or_404(motos, pk=id, usuario=request.user)
            if len(request.FILES) == 0:
                form = MotoForm(request.POST,instance=moto)
                form.save()
            else:         
                moto.imagen = 'Imagenes/' + request.FILES['imagen'].name
                moto.save()
                form = MotoForm(request.POST,instance=moto)
                form.save()
                carpeta_imagen = "BLOG/STATIC/IMAGENES/"
                nombre_imagen = request.FILES["imagen"].name
                img = Image.open(request.FILES["imagen"])
                img.save(carpeta_imagen + nombre_imagen)
                
            return redirect('bmwDetalle', id=id)
        except ValueError:
            return render(request, "bmwEdicion.html", {
                'form': form,
                'error': 'Error en la actualizacion'
            })
        
@login_required
def bmw_eliminar(request, id):
    moto = get_object_or_404(motos, pk=id, usuario=request.user)
    moto.delete()
    return redirect('bmw') 

def otros(request):
    moto = motos.objects.filter(marca='otro')
    return render(request, 'otros.html', {
        'moto': moto
    })

@login_required
def otro_detalle(request, id):
    moto = get_object_or_404(motos, pk=id)
    comentario = Comentario.objects.filter(motos_id=id).values('id', 'descripcion', 'nombre')
    return render(request, 'otrosDetalle.html', {
        'moto': moto,
        'comentario': comentario
    })

@login_required
def otros_edicion(request, id):
    if request.method == 'GET':
        moto = get_object_or_404(motos, pk=id, usuario=request.user)
        form = MotoForm(instance=moto)
        return render(request, "otrosEdicion.html", {
            'form': form
        })
    else:
        try:
            moto = get_object_or_404(motos, pk=id, usuario=request.user)
            if len(request.FILES) == 0:
                form = MotoForm(request.POST,instance=moto)
                form.save()
            else:         
                moto.imagen = 'Imagenes/' + request.FILES['imagen'].name
                moto.save()
                form = MotoForm(request.POST,instance=moto)
                form.save()
                carpeta_imagen = "BLOG/STATIC/IMAGENES/"
                nombre_imagen = request.FILES["imagen"].name
                img = Image.open(request.FILES["imagen"])
                img.save(carpeta_imagen + nombre_imagen)
                
            return redirect('otroDetalle', id=id)
        except ValueError:
            return render(request, "otrosEdicion.html", {
                'form': form,
                'error': 'Error en la actualizacion'
            })
        
@login_required
def otros_eliminar(request, id):
    moto = get_object_or_404(motos, pk=id, usuario=request.user)
    moto.delete()
    return redirect('otros') 

def conocenos(request):
    return render(request, 'acercadenosotros.html')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html',{
        'form': UserRegisterForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'], first_name=request.POST['name'], last_name=request.POST['apellido'])
                user.save()
                login(request, user)
                return redirect('home')
            except:
                return render(request, 'registrarse.html',{
                'form': UserRegisterForm,
                'error': 'Username already exists'
                })
        return render(request, 'registrarse.html',{
                'form': UserRegisterForm,
                'error': 'Password do not match'
                })


def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarsesion.html', {
        'form': CustomAuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarsesion.html', {
            'form': CustomAuthenticationForm,
            'error': 'Username or password is not correct'
            }) 
        else:
            login(request, user)
            return redirect('home')

@login_required
def perfil(request):
    usuario = request.user
    id = request.user.id
    if request.method == 'GET':
        moto = get_object_or_404(User, pk=id)
        form = UserEditForm(instance=moto)
        return render(request, "perfil.html", {
            'form': form
        })
    else:
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            usuario.first_name = miFormulario['first_name'].value()
            usuario.last_name = miFormulario['last_name'].value()
            usuario.email = miFormulario['email'].value()
            usuario.password1 = miFormulario['password1'].value()
            usuario.password2 = miFormulario['password2'].value()
            usuario.save()
            return redirect('home')

@login_required
def cerrarsesion(request):
    logout(request)
    return redirect('home')

@login_required
def subirpublicacion(request):
    if request.method == 'GET':
        return render(request, 'subirPublicacion.html', {
            'form': MotoForm
        })
    else:
        try: 
            form = MotoForm(request.POST)
            moto = form.save(commit=False)
            moto.usuario = request.user
            moto.imagen = 'Imagenes/' + request.FILES['imagen'].name
            moto.save()

            carpeta_imagen = "BLOG/STATIC/IMAGENES/"
            nombre_imagen = request.FILES["imagen"].name
            img = Image.open(request.FILES["imagen"])
            img.save(carpeta_imagen + nombre_imagen)

            return redirect('home')
        except ValueError:
            return render(request, 'subirPublicacion.html', {
                'form': MotoForm,
                'error': 'please provide valide data'
            })
        
@login_required        
def comentario(request, marca, id):
    template = marca + 'Detalle'
    if request.method == 'GET':
        return render(request, 'comentario.html')
    else:
        Comentario.objects.create(motos_id=id,usuario_id=request.user.id , descripcion=request.POST['descripcion'], nombre=request.user)
        return redirect(template,id=id)

@login_required             
def comentarioeditar(request, marca, moto_id, id):
    template = marca + 'Detalle'
    if request.method == 'GET':
        comentario = get_object_or_404(Comentario, pk=id)
        return render(request, 'comentarioEditar.html', {
            'comentario': comentario
        })  
    else:
        comentario = get_object_or_404(Comentario, pk=id)
        descripcion = request.POST['descripcion']
        comentario.descripcion = descripcion
        comentario.save()
        return redirect(template, id=moto_id)          
    
def comentarioeliminar(request, marca, moto_id, id):
    template = marca + 'Detalle'
    comentario = get_object_or_404(Comentario, pk=id)
    comentario.delete()
    return redirect(template, id=moto_id)    