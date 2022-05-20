from django.shortcuts import redirect, render
from django.views import View

from first_app.forms.registration import RegistrationForm


class RegistrationView(View):
    @staticmethod
    def get(request):
        form = RegistrationForm()
        context = {
            'reg_form': form,
        }
        return render(request, 'registration_page.html', context)

    @staticmethod
    def post(request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'reg_form': form,
        }

        return render(request, 'registration_page.html', context)
