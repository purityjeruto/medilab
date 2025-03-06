
from django.contrib import admin
from django.urls import path
from medapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name='home'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('doctors/', views.doctors,name='doctors'),
    path('departments/', views.departments,name='departments'),
    path('appointment/', views.appointment1,name='appointment'),
    path('contact/', views.contact1,name='contact'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),

    path('edit/<int:id>', views.edit,name='edit'),
    path('', views.register,name='register'),
    path('login/', views.login_view,name='login'),

]
