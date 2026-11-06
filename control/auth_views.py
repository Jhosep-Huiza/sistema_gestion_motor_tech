from django.contrib.auth.views import LoginView
from .forms import LoginForm

class MotorTechLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm

    def form_valid(self, form):
        response = super().form_valid(form)
        if not form.cleaned_data.get("remember_me"):
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)
        return response
