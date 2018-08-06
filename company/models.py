from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
import pytz

class Company(models.Model):
    COMPANY = models.CharField(max_length=255, blank=True, null=True)
    TIMESTAMP = models.DateTimeField(blank=True, null=True)
    CUSTOM_FLD_IDS = models.TextField(null=True)
    CUSTOM_FLD_DATA = models.TextField(null=True)
    STAGE_CODE = models.CharField(max_length=255, blank=True, null=True)
    STAGE_DESC = models.CharField(max_length=255, blank=True, null=True)
    USER_CODE = models.IntegerField(null=True)
    TIME_SPEND = models.IntegerField(null=True)
    NOTES = models.TextField(null=True)
    PW_LINK = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.COMPANY)

    class Meta:
        db_table = "companies"


@receiver(pre_save, sender=Company)
def before_save(sender, instance, *args, **kwargs):
    previous_record = sender.objects.filter(COMPANY=instance.COMPANY).order_by('-TIMESTAMP')
    if previous_record:
        current_timestamp = pytz.utc.localize(instance.TIMESTAMP)
        previous_timestamp = previous_record[0].TIMESTAMP
        time_spend = (current_timestamp - previous_timestamp).seconds
        sender.objects.filter(id=previous_record[0].id).update(TIME_SPEND=time_spend)


class CompanyStages(models.Model):
    COMPANY_ID = models.ForeignKey(Company, related_name='company_id', on_delete=models.CASCADE, null=True)
    START_TIME = models.DateTimeField(blank=True, null=True)
    END_TIME = models.DateTimeField(blank=True, null=True)
    STAGE_CODE = models.CharField(max_length=255, blank=True, null=True)
    STAGE_DESC = models.CharField(max_length=255, blank=True, null=True)
    TIME_SPEND = models.IntegerField(null=True)

    def __str__(self):
        return str(self.STAGE_CODE)

    class Meta:
        db_table = "company_stages"