# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import update_view, detail_view 
from . import views

urlpatterns = [
    # path('error/err', views.error,name='err' ),
    path('',views.first,name="home"),

    path('write',views.index,name="write"),
    path('wholediary/',views.diary,name="diary"),
    path('wholediary/<id>',detail_view,name='user_details'),
    path('new/<dd>',views.newdate),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('<id>/', detail_view, name='user_details' ), 
    path('update/<id>/', update_view,name='up' ),
    path('delete/<id>/', views.delo,name='del' ),
    path('delsuccess/<id>/', views.dels,name='dels' ),


] 
