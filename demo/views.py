from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

from django_classified.models import Profile

from django_classified.forms import ProfileForm



@login_required()
def profile_view(request):
	return render(request, 'account/profile.html')
	
#def telephone_view(request):
#	return render(request, 'account/telephone.html')

class telephone_view(UpdateView):
    template_name = 'account/telephone.html'
    form_class = ProfileForm
    success_url = '/accounts/telephone/'

    def get_object(self, queryset=None):
        return Profile.get_or_create_for_user(self.request.user)

    def form_valid(self, form):
        messages.success(self.request, _('Your telephone setting was updated!'))
        return super(telephone_view, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(telephone_view, self).dispatch(*args, **kwargs)
        
		
def profile_redirect(request):
	response = redirect('/accounts/profile/')
	return response
    
def login_view(request):
    response = redirect('/accounts/login/')
    return response
