from django.db import models


class Shipments(models.Model):
    s_name = models.CharField(max_length=32, null=False)
    s_start_ts = models.DateTimeField(null=False)
    s_end_ts = models.DateTimeField(null=True)
    s_done = models.BooleanField(default=False, null=False)
    s_from = models.CharField(null=False)
    s_to = models.CharField(null=False)
