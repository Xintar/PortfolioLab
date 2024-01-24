from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Institution, Donation


class LandingPageView(View):
    def get(self, request):
        institutions = Institution.objects.all()
        donations = Donation.objects.all()
        quality_donations_sum = donations.aggregate(Sum("quantity"))['quantity__sum']
        dontaions_list = []
        for donattion in donations:
            dontaions_list.append(donattion.institution.pk)
        dontaions_list = list(set(dontaions_list))
        instytution_donation = len(dontaions_list)
        ctx = {
            'institutions': institutions,
            'quality_donations': quality_donations_sum,
            'instytution_donation': instytution_donation,
        }
        return render(request, 'index.html', ctx)


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class RegisterPageView(TemplateView):
    template_name = 'register.html'
