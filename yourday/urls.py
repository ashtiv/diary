
from django.contrib import admin
from django.urls import path,include
# from . import views
# from django.conf.urls import (
# handler400, handler403, handler404, handler500
# )

handler400 = 'accounts.views.handler400'
handler403 = 'accounts.views.handler403'
handler404 = 'accounts.views.handler404'
handler500 = 'accounts.views.handler500'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("accounts.urls")),
    path('accounts/',include('django.contrib.auth.urls')),
    # path('error/', accounts.views.error,name='err' ),
    
]