from django.urls import path
from . import views
# registers the ap name space for URL names
app_name = 'my_app'

urlpatterns=[
    path('', views.example_view,name='example'), # domain.omc/my_app
    path('variable',views.variable_view,name='anything')
]
