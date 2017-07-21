from django.conf.urls import url
from .views import Index, Create, Edit, Delete


urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
	url(r'^create$', Create.as_view(), name='create'),
	url(r'^edit$', Edit.as_view(), name='edit'),
	url(r'^delete$', Delete.as_view(), name='delete')
]
