from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Institution, Category


class LandingPageView(View):
    def get(self, request):
        institutions = Institution.objects.all()
        ctx = {
            'institutions': institutions,
        }
        return render(request, 'index.html', ctx)


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class RegisterPageView(TemplateView):
    template_name = 'register.html'
