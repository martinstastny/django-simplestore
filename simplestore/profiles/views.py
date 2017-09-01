from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView

from simplestore.cart.utils import get_cart
from simplestore.checkout.models.order import Order
from .forms import RegistrationForm, LoginForm
from .models import Profile


def profile_index(request):
    return render(request, "profile_index.html")


# Profile Detail
class ProfileDetail(LoginRequiredMixin, DetailView):
    template_name = "profile_detail.html"
    login_url = reverse_lazy('profiles:login')
    model = Profile

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)


# Registration Form
class RegistrationFormView(FormView):
    template_name = "profile_register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        self.profile = form.save()
        self.request.session['user_cart'] = self.request.session.session_key

        user = authenticate(
            email=self.profile.email,
            password=self.request.POST['password1']
        )

        messages.add_message(
            self.request, messages.SUCCESS,
            'You were successfully logged in.'
        )

        login(self.request, user)
        return super(RegistrationFormView, self).form_valid(form)


class UpdateProfileForm(LoginRequiredMixin, UpdateView):
    template_name = 'profile_update.html'
    form_class = RegistrationForm
    model = Profile
    success_url = reverse_lazy('homepage')
    login_url = reverse_lazy('profiles:login')

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)


class ProfileOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'profile_orders.html'
    login_url = reverse_lazy('profiles:login')

    def get_context_data(self, **kwargs):
        context = super(ProfileOrdersView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user.id)

        return context


class ProfileOrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'profile_order_detail.html'
    login_url = reverse_lazy('profiles:login')


# Login
class AuthenticationForm(FormView):
    template_name = 'profile_login.html'
    form_class = LoginForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):

        cart = get_cart(self.request, create=True)
        user = authenticate(email=self.request.POST['email'], password=self.request.POST['password'])

        if user is not None and user.is_active:
            self.request.session['user_cart'] = self.request.session.session_key
            login(self.request, user)

            if cart is not None:
                cart.user = Profile.objects.get(id=user.id)
                cart.save()
                messages.add_message(self.request, messages.SUCCESS, 'You were successfully logged in.')

            return super(AuthenticationForm, self).form_valid(form)

        else:
            response = super(AuthenticationForm, self).form_invalid(form)
            messages.add_message(self.request, messages.WARNING, 'Wrong email or password. Please try again')
            return response


# Logout View
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
