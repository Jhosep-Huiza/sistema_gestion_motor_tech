from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Cliente, Vehiculo, Mecanico, Cita, Diagnostico, Repuesto, OrdenServicio

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
            if isinstance(field.widget, forms.DateInput):
                field.widget.attrs["type"] = "date"
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs["type"] = "time"

class ClienteForm(BaseForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ("created_at",)

class VehiculoForm(BaseForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"

class MecanicoForm(BaseForm):
    class Meta:
        model = Mecanico
        fields = "__all__"

class CitaForm(BaseForm):
    class Meta:
        model = Cita
        fields = "__all__"

class DiagnosticoForm(BaseForm):
    class Meta:
        model = Diagnostico
        fields = "__all__"

class RepuestoForm(BaseForm):
    class Meta:
        model = Repuesto
        fields = "__all__"

class OrdenServicioForm(BaseForm):
    class Meta:
        model = OrdenServicio
        fields = "__all__"

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="Mantener mi cuenta abierta")
