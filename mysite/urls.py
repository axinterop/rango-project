"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect


# @login_required for class based views
def anonymous_required(func):
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL)
        if request.user.is_authenticated:
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view


urlpatterns = [
                  path('polls/', include('polls.urls')),
                  path('admin/', admin.site.urls),
                  path('accounts/login/',
                       LoginView.as_view(redirect_authenticated_user=True),
                       name='login'),
                  path('accounts/register/',
                       anonymous_required(RegistrationView.as_view(success_url='/polls/')),
                       name='django_registration_register'),
                  path('accounts/', include('django_registration.backends.one_step.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
