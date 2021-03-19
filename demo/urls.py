from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, TemplateView


"""
"from django.conf.urls import url" has been removed,
recoded to path() or re_path() as url() is deprecated.
"""

from .views import profile_view
from .views import profile_redirect
from .views import telephone_view


urlpatterns = [
	path('accounts/profile/', profile_view),
	path('accounts/telephone/', telephone_view.as_view(), name='telephone'),
	path('user/profile/', profile_redirect),
    path('', include('django_classified.urls', namespace='django_classified')),
    path('admin/', admin.site.urls),

    # Create custom login page using default 'registration/login.html' template path
    # Login urls here redundant, as dealt with by allauth
    
    #redundant, dealt with in allauth
    #path('email-sent/', TemplateView.as_view(template_name='demo/email_sent.html')),
    
    #allauth
	re_path(r'^accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
