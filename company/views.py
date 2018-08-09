from django.shortcuts import render
from django.db.models import Count
from django.views import View
from company.models import *

class Dashboard(View):
    template = 'company/index.html'

    def get(self, request, *args, **kwargs):
        stage_count = CompanyStages.objects.values('STAGE_DESC').annotate(dcount=Count('STAGE_DESC'))
        print(stage_count)
        return render(request, self.template, {'stage_count': stage_count})