from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, Formulario_Empresa, Formulario_Gestion
from .models import Empresa, Gestion, Recordatorio
from .filters import FiltroEmpresa


def inicio(request):
	records = Empresa.objects.all()
	filtro = FiltroEmpresa(request.GET, queryset=records)
	records = filtro.qs
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Has iniciado sesión!")
			return redirect('inicio')
		else:
			messages.success(request, "Ocurrió un problema al inciar sesión, por favor inténtalo de nuevo...")
			return redirect('inicio')
	else:
		return render(request, 'inicio.html', {'records':records, 'filtro':filtro})



def logout_user(request):
	logout(request)
	messages.success(request, "Has cerrado tu sesión...")
	return redirect('inicio')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Te has registrado correctamente!")
			return redirect('inicio')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Empresa.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Tienes que inciar sesión para ver esta página...")
		return redirect('inicio')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Empresa.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registro eliminado con éxito...")
		return redirect('inicio')
	else:
		messages.success(request, "Tienes que inciar sesión para hacer eso...")
		return redirect('inicio')


def add_record(request):
	form = Formulario_Empresa(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro guardado correctamente...")
				return redirect('inicio')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Tienes que inciar sesión para hacer eso...")
		return redirect('inicio')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Empresa.objects.get(id=pk)
		form = Formulario_Empresa(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "El registro se ha actualizado correctamente!")
			return redirect('inicio')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Tienes que inciar sesión para hacer eso...")
		return redirect('inicio')
	

def nueva_gestion(request):
	form = Formulario_Gestion(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				nueva_gestion = form.save()
				messages.success(request, "Gestión registrada correctamente...")
				return redirect('inicio')  # Cambiar el redireccionamiento a la vista del registro
		return render(request, 'nueva_gestion.html', {'form':form})
	else:
		messages.success(request, "Tienes que iniciar sesión para hacer eso...")
		return redirect('inicio')
	