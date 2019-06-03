from django.conf.urls import url
from . import views
app_name='restapp9'
urlpatterns=[
    url(r'^$',views.input, name='input'),
    url(r'^insert$',views.insert, name='insert'),
    url(r'^display$',views.display, name='display'),
    url(r'^products$',views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)$',views.ProductList1.as_view()),
]