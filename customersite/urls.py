app_name='customersite'
from django.urls import path
from . import views

from django.views.generic.base import TemplateView


urlpatterns=[
   path('',TemplateView.as_view(template_name='customersite/home.html'),name='home'),
   path('homepage',TemplateView.as_view(template_name='customersite/index.html'),name='index'),
   path('login',TemplateView.as_view(template_name='customersite/login.html'),name='login'),
   path('login/',views.login_user,name='login_user'),
   path('logout/',views.logout_user,name='logout'),
   path('register/',views.register_user,name='register'),
   path('record',views.EnterView.as_view(),name='enter'),
   path('records/<int:pk>/',views.customer_record,name='detail'),
   path('record_delete/<int:pk>/',views.delete_record,name='delete'),
   path('record/<int:pk>/update',views.update_record,name='update'),
   path('record/add',views.add_record,name='addrecord'),
  
    
    
    
    
]