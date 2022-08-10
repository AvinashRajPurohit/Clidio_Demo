from django.db import models
# Create your models here.


class Campaigns(models.Model):
    """Dummy Campaigns Model
    """
    campaign_name = models.CharField(blank=True, null=True, max_length=200)
    campaign_type = models.CharField(blank=True, null=True, max_length=200)
    campaign_group = models.CharField(blank=True, null=True, max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.campaign_name} with id {self.id}"
