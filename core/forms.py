from django import forms

from core.models import Campaigns


class CampaignForm(forms.ModelForm):
    """Form for Creating and Updating Campaign
    """
    class Meta:
        model = Campaigns
        fields = ('campaign_name', 'start_date', 'end_date', 'campaign_type', 'campaign_group')
