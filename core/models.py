from django.db import models
from django import forms
# Create your models here.


class Campaigns(models.Model):
    campaign_name = models.CharField(blank=True, null=True, max_length=200)
    campaign_type = models.CharField(blank=True, null=True, max_length=200)
    campaign_group = models.CharField(blank=True, null=True, max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.campaign_name} with id {self.id}"


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaigns
        fields = ('campaign_name', 'start_date', 'end_date', 'campaign_type', 'campaign_group')
