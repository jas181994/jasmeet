from dataclasses import Field
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "LWJ Admin"
admin.site.site_title = "LWJ Admin"
admin.site.index_title = "Welcome to Learn with Jas"




urlpatterns = [
    

    path("",views.index,name='home'), 
    path("about",views.about,name='about'),
    path("Field",views.Field,name='Fields')
]