from django.contrib import admin
from django.urls import path
from krushigandha import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('home/',views.home),
    path('header/', views.header),
    path('footer/', views.footer),
    path('overview/', views.overview),
    path('aboutCompany/', views.aboutCompany),
    path('overview3/', views.overview3),
    path('benefit/', views.benefit),
    path('overall/', views.overall),
    path('products/', include('products.urls')),
    path('gallary/', views.gallary),
    path('contact/', views.contact, name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('carrier/', views.carrier, name='carrier'),
    path('order/', views.order, name='order'),  # Add this line
    path('order_done/', views.order_done, name='order_done'),
    path('profile/', views.profile),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
