from django.urls import path
from . import views
#from .views import UserRegisterView

urlpatterns=[
    #path('pull_data_from_api/',views.pull_data_from_api,name='pull_data_from_api'),
    #path('api/user/register/',UserRegisterView.as_view(),name='user_register'),
    #path('register/', views.register, name='register'),
    path('admissionportal',views.admissionpage),
    path('admissioncode',views.admissioncode),
]