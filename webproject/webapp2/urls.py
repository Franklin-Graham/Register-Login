
from django.urls import path
from .  import views

urlpatterns = [
    path('register',views.reg,name="reg"),
    path('login',views.log,name="log"),
    path('logout',views.out,name="out")

]