from django.urls  import path

from . import views

urlpatterns = [
	path('',views.loginUser,name="login"),
	path('validateUser/',views.validateUser,name="session"),	
]