from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .forms import UserRegistrationForm

# Create your views here.
from django.views.generic import RedirectView, FormView
from django.conf import settings

import logging

logger = logging.getLogger(__name__)

@method_decorator(login_required, name='dispatch')
class HomePageView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        logger.info('User has redirected to Calendar:list')
        return reverse_lazy("calendar:list")#"/timetable/list"



class RegisterFormView(FormView):
    form_class = UserRegistrationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    '''def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return self.get(request, *args, **kwargs)'''



    def form_valid(self, form):
        logger.debug("client has registered")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.debug("client tried to register")
        return super().form_invalid(form)







