from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.register, name='registration'),
    path('login/', views.login, name='login'),
    path('landing/', views.landing, name='landing'),
    path('import-files/', views.importfiles, name='import-files'),
]