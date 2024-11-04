# admin_portal/views.py
from django.shortcuts import render, redirect
from .models import Route, ThirdPartyLogistics, Driver, DelayReport
from .forms import RouteForm, ThirdPartyLogisticsForm
from .models import Driver  # Ensure GPSLocation is properly imported
from .forms import RouteForm, CheckpointForm, Checkpoint,DriverForm


from django.shortcuts import get_object_or_404
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for rendering without a window

import matplotlib.pyplot as plt
import io
import urllib
import base64
from django.shortcuts import render
from .models import Route
from io import BytesIO
from django.db.models import Count

# admin_portal/views.py
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# View for the admin home page
def admin_home(request):
    return render(request, 'admin_portal/admin_home.html')  # Create an HTML template for this view



# View to list and manage routes
from django.db.models import Prefetch

# View to list and manage routes
import io
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import Route

def route_list(request):
    routes = Route.objects.all()

    # Example data for the pie chart (e.g., route distribution by number of checkpoints)
    route_names = [route.route_name for route in routes]
    checkpoint_counts = [route.checkpoints.count() for route in routes]

    # Create the pie chart
    plt.figure(figsize=(6, 6))
    wedges, texts, autotexts = plt.pie(
        checkpoint_counts, 
        labels=route_names, 
        autopct=lambda p: '{:.0f} checkpoints'.format(p * sum(checkpoint_counts) / 100),  # Show the number of checkpoints
        startangle=140, 
        colors=plt.cm.Paired.colors
    )

    # Add a legend to the pie chart
    plt.legend(wedges, route_names, title="Routes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Ensure that pie is drawn as a circle
    plt.axis('equal')

    # Save the figure to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64 string for embedding in HTML
    chart_url = base64.b64encode(image_png).decode('utf-8')
    chart_url = 'data:image/png;base64,' + chart_url

    context = {
        'routes': routes,
        'chart_url': chart_url,
    }

    return render(request, 'admin_portal/route_list.html', context)



def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        checkpoint_count = int(request.POST.get('checkpoint_count', 0))

        if form.is_valid():
            route = form.save()  # Save the route first
            
            # Loop through each checkpoint and save it to the database
            for i in range(checkpoint_count):
                checkpoint_name = request.POST.get(f'checkpoint_{i+1}_name')
                load_location = request.POST.get(f'checkpoint_{i+1}_load_location')
                unload_location = request.POST.get(f'checkpoint_{i+1}_unload_location')
                load_tonnes = request.POST.get(f'checkpoint_{i+1}_load_tonnes')

                if checkpoint_name and load_location and unload_location and load_tonnes:
                    load_tonnes = float(load_tonnes) if load_tonnes else 0.0
                    checkpoint = Checkpoint(
                        route=route,
                        name=checkpoint_name,
                        load_location=load_location,
                        unload_location=unload_location,
                        load_tonnes=load_tonnes,
                        order=i + 1
                    )
                    checkpoint.save()
                else:
                    messages.error(request, f"Missing data for checkpoint {i+1}")

            messages.success(request, 'Route and checkpoints added successfully.')
            return redirect('route_list')
        else:
            messages.error(request, 'Error in form submission. Please correct the errors.')
            print(form.errors)  # Debugging: print form errors
    else:
        form = RouteForm()

    return render(request, 'admin_portal/add_route.html', {'form': form})


def delay_reports(request):
    reports = DelayReport.objects.all()
    
    # Example: Create a chart for delay reasons
    reasons_count = reports.values('reason').annotate(count=Count('id'))  # Use Count from django.db.models

    # Generate the chart
    plt.figure(figsize=(10, 5))
    plt.bar([reason['reason'] for reason in reasons_count], [reason['count'] for reason in reasons_count])
    plt.title('Delay Reasons Distribution')
    plt.xlabel('Reason')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    
    # Save to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    
    # Encode to base64
    chart_url = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'admin_portal/delay_reports.html', {'reports': reports, 'chart_url': chart_url})


# View to edit a route
def edit_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm(instance=route)
    return render(request, 'admin_portal/edit_route.html', {'form': form})


# View to delete a route
def delete_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.delete()
    return redirect('route_list')


# admin_portal/views.py
def assign_driver(request):
    # Logic for assigning a driver goes here
    # For simplicity, you could list drivers and let the admin select
    drivers = Driver.objects.all()  # Fetch all drivers
    routes = Route.objects.all()  # Fetch all routes
    return render(request, 'admin_portal/assign_driver.html', {'drivers': drivers, 'routes': routes})




def third_party_requests(request):
    # Fetch third-party logistics requests along with the related route information
    requests = ThirdPartyLogistics.objects.select_related('route').all()
    return render(request, 'admin_portal/third_party_requests.html', {'requests': requests})




def approve_3pl_request(request, id):
    request_to_approve = get_object_or_404(ThirdPartyLogistics, id=id)
    request_to_approve.is_approved = True
    request_to_approve.save()
    return redirect('third_party_requests')  # Adjust as necessary

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'admin_portal/driver_list.html', {'drivers': drivers})
def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver added successfully.')
            return redirect('driver_list')
        else:
            messages.error(request, 'Error in form submission. Please correct the errors.')
    else:
        form = DriverForm()
    return render(request, 'admin_portal/add_driver.html', {'form': form})

def driver_location(request, driver_id):
    driver = Driver.objects.get(id=driver_id)
    return render(request, 'admin_portal/driver_location.html', {'driver': driver})





from shapely.geometry import Point, Polygon
import json

def is_within_geofence(driver_location, geofence):
    # Convert driver_location to a Point
    driver_point = Point(driver_location['longitude'], driver_location['latitude'])
    
    # Load the polygon from JSON
    polygon_coords = json.loads(geofence.polygon)
    geofence_polygon = Polygon(polygon_coords)
    
    # Check if the driver point is within the geofence
    return geofence_polygon.contains(driver_point)