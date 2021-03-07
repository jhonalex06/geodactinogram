# Users views

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

#Models 
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Forms
from users.form import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    # User detail view
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    # Sign up view

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Save form data 
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    # Update profile view
    template_name = 'users/update_profile.html'
    model =Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self, queryset=None):
        # return users profile 
        return self.request.user.profile

    def get_success_url(self):
        # return to users profile
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
    # Login view
    template_name = 'users/login.html'

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')