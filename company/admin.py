from django.contrib import admin
from company.models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
        fields = ('id', 'COMPANY', 'TIMESTAMP', 'CUSTOM_FLD_IDS', 'CUSTOM_FLD_DATA','STAGE_CODE','STAGE_DESC','USER_CODE',
                  'NOTES','PW_LINK',)


class CompanyAdmin(ImportExportActionModelAdmin):
    resource_class = CompanyResource


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyStages)