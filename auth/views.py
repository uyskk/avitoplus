from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import RegistrationForm


def register_view(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)
            messages.success(request, "Вы успещно зарегестрировались")

            return redirect(reverse_lazy("login"))

        messages.error(request, "Регистрация не удалась, возможно вы неверно указали информацию")

        return render(request, 'registration/register.html', context={'form': form})

    form = RegistrationForm()

    return render(
        request=request,
        template_name="registration/register.html",
        context={
            "form": form
        }
    )
