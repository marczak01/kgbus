from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

app_name = 'main'

urlpatterns =[
    path('', views.index, name='main'),
    path('send/', views.send_mail, name="send_email"),
]