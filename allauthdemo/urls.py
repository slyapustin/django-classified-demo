from django.contrib import admin
#from django.conf.urls import url, include
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, TemplateView


"""
#from django.conf.urls import url, include

This is redundant, as docs indicate that "path()" should be used
rather than "url()".

"""
#from django_classified import views
#from . import settings
#from mysite.core import views as core_views

from .views import profile_view
from .views import profile_redirect
from .views import telephone_view


urlpatterns = [
	#path('accounts/profile/', auth_views.LoginView.as_view(template_name='account/profile.html'), name='profile'),
	path('accounts/profile/', profile_view),
	#path('user/telephone/', views.ProfileView.as_view(), name='profile'),
	path('accounts/telephone/', telephone_view.as_view(), name='telephone'),
	path('user/profile/', profile_redirect),
    path('', include('django_classified.urls', namespace='django_classified')),
    path('social/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),

    # Create custom login page using default 'registration/login.html' template path
    # Login urls here redundant, as dealt with by allauth
    
    #redundant, dealt with in allauth
    #path('email-sent/', TemplateView.as_view(template_name='demo/email_sent.html')),
    
    #allauth
	re_path(r'^accounts/', include('allauth.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
