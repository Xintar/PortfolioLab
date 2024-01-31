from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import LoginForm, UserForm
from .models import Institution, Donation, Category


class LandingPageView(View):
    template_name = "index.html"

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
        return render(request, self.template_name, ctx)


class AddDonationView(View):
    template_name = 'form.html'

    def get(self, request):
        if request.user.is_authenticated:
            categories = Category.objects.all()
            institutions = Institution.objects.all()
            ctx = {
                'categories': categories,
                'institutions': institutions
            }
            return render(request, self.template_name, ctx)
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            ctx = {

            }
            return render(request, self.template_name, ctx)
        else:
            return redirect('login')


class LoginPageView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('landing')
        else:
            form = LoginForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('landing')
            else:
                comment = "Brak użytkownika w bazie, zarejestruj się."
                return redirect('register')
                # TODO ustawić z przekierowanie z komentarzem
                # return redirect('register', comment=comment)
        else:
            form = LoginForm()
            ctx = {
                'form': form,
                'comment': "Błędne dane logowania"
            }
            return render(request, self.template_name, ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing')


class RegisterPageView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('landing')
        else:
            comment = request.GET.get('comment', '')
            form = UserForm()
            ctx = {
                'comment': comment,
                'form': form,
            }
            return render(request, self.template_name, ctx)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
        else:
            form = UserForm()
            ctx = {
                'form': form,
                'comment': "Błąd rejestracji",
            }
            return render(request, 'login.html', ctx)
