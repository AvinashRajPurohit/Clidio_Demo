from datetime import datetime
from logging import Logger
from typing import Union

from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from core.models import Campaigns
from core.forms import CampaignForm

# Create your views here.
campaign_logger: Logger = Logger("Campaign Views")


class HomeView(View):
    """Django class based view:
        1. get campaign
        2. create campaign
        3. update campaign
    """
    def get(self, request):
        """get single campaign
        :param request: django request
        :return: render
        """
        context: dict = {}
        campaign_id: Union[str, None] = request.GET.get("campaign_id", None)
        if campaign_id is not None:
            try:
                campaign: Campaigns = get_object_or_404(Campaigns, id=campaign_id)
            except Http404 as e:
                campaign_logger.error(str(e))
                return HttpResponse("Campaign Not Found")

            context: dict = {
                "update": True,
                "campaign": campaign
            }
        return render(request, 'core/home.html', context)

    def post(self, request):
        data: dict = request.POST
        campaign_id: Union[str, None] = request.GET.get("campaign_id", None)
        if data.get("updating") is None:
            # Creating campaign
            campaign_name = self.create_campaign(data)
            messages.success(request, f"Campaign '{campaign_name}' is created...")
            return redirect('campaigns-list')
        else:
            # Updating campaign
            campaign_name = self.update_campaign(data, campaign_id)
            messages.warning(request, f"Campaign '{campaign_name}' is successfully updated...")
            return redirect('campaigns-list')

    @staticmethod
    def create_campaign(data):
        """function to create campaign and redirect to campaign list
        """
        form: CampaignForm = CampaignForm(data)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return f.campaign_name

    @staticmethod
    def update_campaign(data, campaign_id):
        """function to update campaign and redirect to campaign list
        """
        campaign: Campaigns = get_object_or_404(Campaigns, id=campaign_id)
        form: CampaignForm = CampaignForm(data, instance=campaign)
        if form.is_valid():
            f = form.save()
            f.updated_at = datetime.now()
            f.save()
            return f.campaign_name


def list_campaigns(request):
    """django function based view for listing all the campaigns
    :param request: django request
    :return: render
    """
    campaigns: list[Campaigns] = Campaigns.objects.all()
    context: dict = {
        'campaigns': campaigns
    }
    return render(request, 'core/list_campaigns.html', context)


def delete_campaign(request, campaign_id: str):
    """django function based view for deleting a campaign
    :param request: django request
    :param campaign_id: id of deleting campaign
    :return: render
    """
    campaign: Campaigns = get_object_or_404(Campaigns, id=campaign_id)
    campaign.delete()
    messages.warning(request, f"Campaign '{campaign.campaign_name}'"
                              f" is successfully deleted...")
    return redirect('campaigns-list')
