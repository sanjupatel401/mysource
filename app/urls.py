
from django.urls import path,include
from . import views
urlpatterns = [
  
    path('',views.index,name='index'),
    path('up/',views.up_project,name='upload_project'),
    path('All_projects/',views.all_projetcs,name='all_project'),
    path('search/',views.search,name='search'),
    path('login_form/',views.login_form,name='login_form'),

]
