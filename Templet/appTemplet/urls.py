from django.urls import path
from appTemplet import views

app_name='Basic_app'

urlpatterns = [
    path('relative/',views.relative , name='relative'),
    path('other/',views.other,name='other')

]
