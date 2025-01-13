from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.opportunity_list, {'category': 'job'}, name='jobs'),
    path('hackathons/', views.opportunity_list, {'category': 'hackathon'}, name='hackathons'),
    path('internships/', views.opportunity_list, {'category': 'internship'}, name='internships'),
    path('mock-tests/', views.mock_tests, name='mock_tests'),
    path('activity-points/', views.activity_points, name='activity_points'),
    path('apply/<int:opportunity_id>/', views.apply, name='apply'),
]