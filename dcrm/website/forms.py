from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Empresa, Gestion, Recordatorio


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Letras, digitos y @/./+/-/_.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Requerimiento seguridad 1</li><li>Requerimiento seguridad 2</li><li>Requerimiento seguridad 3</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingresar la misma contraseña para verificar</small></span>'	


# Tuplas para validación de datos
REGIONES_CHILE = [
    ('XV', 'Arica y Parinacota'),
    ('I', 'Tarapacá'),
    ('II', 'Antofagasta'),
    ('III', 'Atacama'),
    ('IV', 'Coquimbo'),
    ('V', 'Valparaíso'),
    ('VI', 'Libertador General Bernardo O\'Higgins'),
    ('VII', 'Maule'),
    ('VIII', 'Biobío'),
    ('IX', 'La Araucanía'),
    ('XIV', 'Los Ríos'),
    ('X', 'Los Lagos'),
    ('XI', 'Aysén del General Carlos Ibáñez del Campo'),
    ('XII', 'Magallanes y de la Antártica Chilena'),
    ('RM', 'Región Metropolitana de Santiago'),
    ('XVI', 'Ñuble'),
]

TIPO_GESTION =[
	('LL', "Llamada Telefónica"),
	('VL', "Videollamada"),
	('CE', 'Correo Electrónico'),
	('VI', 'Visita')
]

ESTADO_GESTION = [
	('TE', 'Terminada'),
	('ES', 'En curso'),
	('SR', 'Sin respuesta'),
]

# Fomularios
class Formulario_Empresa(forms.ModelForm):
	id_empleador = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ID Empleador", "class":"form-control"}), label="")
	razon_social = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Razon Social", "class":"form-control"}), label="")
	celular = forms.IntegerField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono Celular", "class":"form-control"}), label="")
	telefono = forms.IntegerField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono Fijo", "class":"form-control"}), label="")
	email = forms.EmailField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	direccion = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Dirección", "class":"form-control"}), label="")
	comuna = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Comuna", "class":"form-control"}), label="")
	region = forms.ChoiceField(required=False, choices=REGIONES_CHILE, widget=forms.Select(attrs={"class":"form-control"}), label="")
	cant_afiliados = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Cantidad Afiliados", "class":"form-control"}), label="")

	class Meta:
		model = Empresa
		exclude = ("user",)


class Formulario_Gestion(forms.ModelForm):
	#empresa = forms.ChoiceField(required=True, widget=forms.Select(attrs={"class":"form-control"}), label="")
	tipo = forms.ChoiceField(required=True, choices=TIPO_GESTION, widget=forms.Select(attrs={"class":"form-control"}), label="")
	estado = forms.ChoiceField(required=True, choices=ESTADO_GESTION, widget=forms.Select(attrs={"class":"form-control"}), label="")
	comentarios = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Comentarios", "class":"form-control"}), label="")

	class Meta:
		model = Gestion
		exclude = ("user",)

#OpcionesDeFiltrado como una lista de tuplas que representan las opciones en la lista desplegable. 
# En el ejemplo, hemos agregado una opción "Todos" para que el usuario pueda seleccionar para mostrar todos los registros sin filtrar.
