from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Driver(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Route(models.Model):
    route_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    assigned_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Ensure this field exists
    created_at = models.DateTimeField(default=timezone.now)  # Ensure this field exists

    def __str__(self):
        return self.route_name

class Checkpoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='checkpoints')
    name = models.CharField(max_length=255)
    load_location = models.CharField(max_length=255)
    unload_location = models.CharField(max_length=255)
    load_tonnes = models.DecimalField(max_digits=10, decimal_places=2)  # Load in tonnes
    order = models.PositiveIntegerField()  # Maintain the order of checkpoints

    def __str__(self):
        return self.name
    
class ThirdPartyLogistics(models.Model):
    company_name = models.CharField(max_length=255)
    request_load = models.FloatField(help_text="Load capacity requested in tonnes")
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.request_load} tonnes"

class DelayReport(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delay by {self.driver.name} on {self.route.route_name}"



class Geofence(models.Model):
    name = models.CharField(max_length=100)
    polygon = models.TextField()  # Store coordinates as JSON or a similar format
    created_at = models.DateTimeField(auto_now_add=True)