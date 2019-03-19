"""tilenga_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from . views import index

from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/',include(('authentication.urls','authentication'), namespace='authentication')),
    path('orders/', include(('order.urls','order'), namespace='order')),
    path('service/', include(('service.urls','service'), namespace='service')),
    path('waste-collection/', include(('waste_collection.urls','waste_collection'), namespace='waste_collection')),
    path('waste-reception/', include(('waste_reception.urls','waste_reception'), namespace='waste_reception')),
    path('waste-treatment/', include(('waste_treatment.urls','waste_treatment'), namespace='waste_treatment')),
    path('waste/', include(('waste.urls','waste'), namespace='waste')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logistics/', include(('logistics.urls', 'logistics'), namespace='logistics')),
    
] 

urlpatterns += staticfiles_urlpatterns()
