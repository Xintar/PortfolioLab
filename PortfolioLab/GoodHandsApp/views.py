from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'index.html'


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class RegisterPageView(TemplateView):
    template_name = 'register.html'
