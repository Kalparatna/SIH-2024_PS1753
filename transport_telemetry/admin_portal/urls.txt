# admin_portal/urls.py
from django.urls import path
from . import views 
from .views import (
    admin_home,
    route_list,
    add_route,
    third_party_requests,  # Ensure this is imported
    delay_reports,
    edit_route,
    delete_route,
    assign_driver,
)

urlpatterns = [
    path('', admin_home, name='admin_home'),
    path('routes/', route_list, name='route_list'),
    path('routes/add/', add_route, name='add_route'),
    path('routes/edit/<int:route_id>/', edit_route, name='edit_route'),
    path('routes/delete/<int:route_id>/', delete_route, name='delete_route'),
    path('3pl_requests/', third_party_requests, name='third_party_requests'),  # Add this line
    path('delay_reports/', delay_reports, name='delay_reports'),
    path('assign_driver/', assign_driver, name='assign_driver'),
    path('approve_3pl_request/<int:id>/', views.approve_3pl_request, name='approve_3pl_request'),

    
    path('drivers/', views.driver_list, name='driver_list'),
    path('drivers/add/', views.add_driver, name='add_driver'),
    path('drivers/<int:driver_id>/', views.driver_location, name='driver_location'),
]
    

