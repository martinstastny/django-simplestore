from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import DetailView, ListView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .models import Profile
from cart.models import Cart
from checkout.models.order import Order

def profile_index(request):
    return render(request, "profile_index.html")

# Profile Detail
class ProfileDetail(DetailView):
    template_name = "profile_detail.html"
    model = Profile

# Registration Form
class RegistrationFormView(FormView):
    template_name = "profile_register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        self.profile = form.save()
        self.request.session['user_cart'] = self.request.session.session_key
        user = authenticate(email=self.profile.email, password=self.request.POST['password1'])
        messages.add_message(self.request, messages.SUCCESS, 'You were sucessfully logged in.')
        login(self.request, user)
        return super(RegistrationFormView, self).form_valid(form)


class UpdateProfileForm(UpdateView):
    template_name = "profile_update.html"
    form_class = RegistrationForm
    model = Profile
    success_url = reverse_lazy('homepage')


class ProfileOrdersView(ListView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super(ProfileOrdersView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user.id)

        return context

# Login
class AuthenticationForm(FormView):
    template_name = "profile_login.html"
    form_class = LoginForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):

        cart = Cart.objects.get(session_key=self.request.session.session_key)
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

