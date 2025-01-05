from django.urls import include, re_path, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    re_path('', include('django_classified.urls', namespace='django_classified')),
    re_path('social/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),

    # Create custom login page using default 'registration/login.html' template path
    path('login/', auth_views.LoginView.as_view(template_name='demo/login.html'), name='login'),
    path('email-sent/', TemplateView.as_view(template_name='demo/email_sent.html'))
]
