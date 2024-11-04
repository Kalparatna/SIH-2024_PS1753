# admin_portal/admin.py
from django.contrib import admin
from .models import Driver, Route, ThirdPartyLogistics, DelayReport

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'is_available')

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'origin', 'destination', 'assigned_driver', 'is_active', 'created_at')

@admin.register(ThirdPartyLogistics)
class ThirdPartyLogisticsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'request_load', 'route', 'is_approved', 'created_at')

@admin.register(DelayReport)
class DelayReportAdmin(admin.ModelAdmin):
    list_display = ('driver', 'route', 'reason', 'reported_at')
