from django.conf.urls import url

from .views import index, Login, Logout, singup

urlpatterns = [
    url(r'^$', index.as_view(), name='index'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^singup$', singup.as_view(), name='singup'),
]
