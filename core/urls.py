from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
     # SERVICES
    path(
        'services/it-solutions/',
        ITSolutionsView.as_view(),
        name='it_solutions'
    ),

    path(
        'services/electrical-engineering/',
        ElectricalEngineeringView.as_view(),
        name='electrical_engineering'
    ),

    path(
        'services/security-systems/',
        SecuritySystemsView.as_view(),
        name='security_systems'
    ),

    path(
        'services/telecommunications/',
        TelecommunicationsView.as_view(),
        name='telecommunications'
    ),

    path(
        'services/maintenance/',
        MaintenanceView.as_view(),
        name='maintenance'
    ),

    # COMPANY
    path(
        'company/about/',
        AboutView.as_view(),
        name='about'
    ),

    path(
        'company/projects/',
        ProjectsView.as_view(),
        name='projects'
    ),

    path(
        'company/team/',
        TeamView.as_view(),
        name='team'
    ),

    path(
        'company/careers/',
        CareersView.as_view(),
        name='careers'
    ),

    path(
        'company/news/',
        NewsView.as_view(),
        name='news'
    ),
    path(
        'company/contact/',
        ContactView.as_view(),
        name='contact'
    ),
]