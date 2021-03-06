from django.urls import path
from .views import GigListView, GigDetailView, GigPostView, VenueListView, VenueDetailView

urlpatterns = [
    path('gigs/', GigListView.as_view()),
    path('gigs/create/', GigPostView.as_view()),
    path('gigs/<int:pk>/', GigDetailView.as_view()),
    path('venues/', VenueListView.as_view()),
    path('venues/<int:pk>/', VenueDetailView.as_view())
]