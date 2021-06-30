from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.method,name='hari'),
    url(r'^submit',views.submit,name='submit')
]