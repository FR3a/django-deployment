from django.conf.urls import url
from . import views

# Templates URLS !
app_name = 'fiveApp'

urlpatterns = [
    url(r'^registers/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]