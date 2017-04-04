from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .models import Profile
from cart.models import Cart
from cart.mixins import get_cart

def profile_index(request):
    return render(request, "profile_index.html")

# Profile Detail
class ProfileDetail(DetailView):
    template_name = "profile_detail.html"
    model = Profile

# Registration Form
class RegistrationForm(FormView):
    template_name = "profile_register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        self.profile = form.save()
        self.request.session['user_cart'] = self.request.session.session_key
        user = authenticate(email=self.profile.email, password=self.request.POST['password1'])
        messages.add_message(self.request, messages.SUCCESS, 'You were sucessfully loged in')
        login(self.request, user)
        return super(RegistrationForm, self).form_valid(form)


class UpdateProfileForm(UpdateView):
    template_name = "profile_update.html"
    form_class = RegistrationForm
    model = Profile
    success_url = reverse_lazy('homepage')

# Login
class AuthenticationForm(FormView):
    template_name = "profile_login.html"
    form_class = LoginForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        try:
            cart = Cart.objects.get(session_key=self.request.session.session_key)
        except:
            cart = None

        user = authenticate(email=self.request.POST['email'], password=self.request.POST['password'])

        if user is not None and user.is_active:
            self.request.session['user_cart'] = self.request.session.session_key
            login(self.request, user)
            if cart is not None:
                cart.user = Profile.objects.get(id=user.id)
                cart.save()
            messages.add_message(self.request, messages.SUCCESS, 'You were sucessfully logged in.')
            return super(AuthenticationForm, self).form_valid(form)
        else:
            response = super(AuthenticationForm,self).form_invalid(form)
            messages.add_message(self.request, messages.WARNING, 'Wrong email or password. Please try again')
            return response

# Logout View
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

