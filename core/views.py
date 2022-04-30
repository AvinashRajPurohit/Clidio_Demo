from typing import Union

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from core.models import Campaigns, CampaignForm
from datetime import datetime

# Create your views here.


class HomeView(View):

    def get(self, request):
        campaign_id: Union[str, None] = request.GET.get("campaign_id", None)

        if campaign_id is not None:
            campaign = get_object_or_404(Campaigns, id=campaign_id)

            context = {
                "update": True,
                "campaign": campaign
            }
        else:
            context = {}

        return render(request, 'core/home.html', context)

    def post(self, request):
        data: dict = request.POST
        campaign_id: Union[str, None] = request.GET.get("campaign_id", None)
        try:
            if data.get("updating", None) is None:
                form = CampaignForm(data)
                if form.is_valid():
                    f = form.save(commit=False)
                    f.save()
                    messages.success(request, f"Campaign '{f.campaign_name}' is created...")
                    return redirect('campaigns-list')
            else:
                campaign = get_object_or_404(Campaigns, id=campaign_id)
                form = CampaignForm(data, instance=campaign)
                if form.is_valid():
                    f = form.save()
                    f.updated_at = datetime.now()
                    f.save()
                    messages.warning(request, f"Campaign '{campaign.campaign_name}' is successfully updated...")
                    return redirect('campaigns-list')
        except Exception as e:
            print(e)
            return HttpResponse("Something went wrong...")


def list_campaigns(request):
    campaigns = Campaigns.objects.all()
    context = {
        'campaigns': campaigns
    }
    return render(request, 'core/list_campaigns.html', context)


def delete_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaigns, id=campaign_id)
    campaign.delete()
    messages.warning(request, f"Campaign '{campaign.campaign_name}' is successfully deleted...")
    return redirect('campaigns-list')
