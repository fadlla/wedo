from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView

from booking.admin import BookingsAdmin

# Impor kelas BookingsAdmin dari file admin.py
from django.urls import path
from jet.dashboard.dashboard import DefaultAppIndexDashboard
# from jet.dashboard.dashboard_modules import google_analytics_views


# admin.site.index_template = 'dashboard/index.html'
# admin.site.app_index_template = 'dashboard/app_index.html'

urlpatterns = [
    # ... url lainnya ...
    # path('admin/', admin.site.urls),
    # path('admin/', views.admin_dashboard, name='dashboard_admin'),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include(('jet.dashboard.urls', 'jet-dashboard'), namespace='jet-dashboard')),

    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('wedding/', include('wedding.urls')),
    path('accounts/', include('accounts.urls')),
    path('socialaccounts/', include('allauth.urls')),
    path('booking/', include('booking.urls')),
    # path untuk halaman kelola orderan
    # path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


