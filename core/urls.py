from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import RegisterFormView

urlpatterns = [
    url(r'login/$', login, {'template_name': 'auth/login.html'}, name="login"),
    url(r'register/$', RegisterFormView.as_view(), name="register"),
    url(r'logout/$', logout, {'next_page': '/'}, name="logout")
]
