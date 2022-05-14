from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext_lazy as _


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        context = _('welcome')
        return render(request, self.template_name, {'home_context': context})
