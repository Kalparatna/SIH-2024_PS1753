# Road Transport Network Telematics Solution
🔗 **[Project Overview](https://drive.google.com/file/d/1vJBuHQ_-8Oqy2e5QJNpPtCkkEivZcumo/view?usp=sharing)**
## Background

The Department of Posts operates 76 national routes under the All India Road Transport Network (RTN). Commercial trucks of 5-14 tonnes capacity ply on these routes carrying parcels and mail. Additionally, there are state or intra-circle routes operated through a combination of commercial and departmental trucks for carrying parcels and mail.

The RTN trucks, operating on various routes, touch intermediate points, where parcels and mail are off-loaded and loaded. The capacity utilization of the trucks fluctuates depending upon the volume of parcels/mail being carried. Real-time data is essential for optimal utilization of truck capacity and adequate planning.

Integration with third-party logistics (3PL) partners for capacity sharing via API is required to monetize spare capacity. The system must allow for real-time monitoring of the trucks, tracking delays, and managing dispatch schedules.

## Expected Solution

The solution should be based on GPS and GIS technology, with strong integration for route optimization, live tracking, monitoring, and alerts for delays or detours. The solution should be capable of:
- Real-time monitoring of truck locations.
- Managing capacity utilization and optimizing routes.
- Triggering alerts for delays and detours.
- Automatically updating schedules and dispatch plans based on real-time data.
- Generating automated reports with relevant visualizations.

## Key Features

### Admin Home Page
- A simple landing page directing users to other sections of the admin portal.

### Route Management
- View the list of routes with a pie chart displaying the distribution of checkpoints across routes.
- Add, edit, or delete routes, including associated checkpoints.
- Visualize the number of checkpoints associated with each route, helping optimize the route network.

### Delay Reports
- A section to view and analyze delay reports, including a bar chart showing delay reasons (e.g., traffic, breakdowns).
- Insights into road transport inefficiencies and potential areas for improvement.

### Driver Management
- View and manage drivers in the system.
- Assign drivers to routes via an admin interface.
- View driver locations for real-time tracking of trucks.
- Efficiently manage trucking operations by ensuring drivers are assigned to the right routes.

### Third-Party Logistics (3PL) Requests
- Manage 3PL requests, including approval or rejection.
- The system integrates 3PL requests with routes, ensuring that third-party logistics providers can access the correct information.

### Geofencing Integration
- Check if a driver's location is within a specified geofence.
- Use geofencing to monitor whether trucks are within designated regions or routes, improving real-time monitoring and security.

## How This Supports the SIH Problem Statement

- **Route Optimization**: The dashboard allows admins to view and manage routes, checkpoints, and delays to help optimize trucking routes and improve overall efficiency.
- **Live Tracking and Monitoring**: The system supports real-time tracking of drivers and trucks, providing full visibility of the transport network.
- **Optimal Capacity Utilization**: The dashboard includes analytics (pie charts, delay reports) to track and optimize truck capacity utilization.
- **Appropriate Response**: The system allows admins to quickly respond to logistics needs by approving/rejecting 3PL requests, assigning drivers, and adjusting schedules based on real-time data.

## Technologies Used
- **Django**: Web framework for backend logic and views.
- **Matplotlib**: For creating charts and visualizations.
- **Shapely**: For geospatial operations and geofencing.
- **Firebase**: For real-time data storage and synchronization.
- **Google Maps API / GPS**: For live tracking of truck locations.

## Setup Instructions

1. Clone the repository to your local machine.
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set up your Firebase configuration and other environment variables.
4. Run the Django server:
    ```
    python manage.py runserver
    ```
5. Access the admin portal at `http://127.0.0.1:8000/admin/`.
