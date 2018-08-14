from django.shortcuts import render
from django.db.models import Count
from django.views import View
from company.models import *
from django.http import JsonResponse


def get_stage_percent(request):
    stage_count = CompanyStages.objects.values('STAGE_DESC').annotate(Percent=Count('STAGE_DESC'))
    total_stages = CompanyStages.objects.all().count()

    for index,stage in enumerate(stage_count):
        stage_percent = stage['Percent'] / total_stages
        stage_count[index]['Percent'] =  stage_percent
    return JsonResponse(list(stage_count), safe=False)

class Dashboard(View):
    template = 'company/index.html'

    def get(self, request, *args, **kwargs):
        stage_count = CompanyStages.objects.values('STAGE_DESC').annotate(dcount=Count('STAGE_DESC'))
        return render(request, self.template, {'stage_count': stage_count})