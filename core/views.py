from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import UserRegistrationForm

# Create your views here.
from django.views.generic import RedirectView, FormView
from django.conf import settings


class HomePageView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return "/timetable/list"



class RegisterFormView(FormView):
    form_class = UserRegistrationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return self.get(request, *args, **kwargs)



