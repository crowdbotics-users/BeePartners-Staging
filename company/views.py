from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Dashboard(View):
    template = 'company/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})