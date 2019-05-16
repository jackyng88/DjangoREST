from django.urls import path
from jobs.api.views import JobOfferDetailAPIView, JobOfferListCreateAPIView


urlpatterns = [
    path('jobs/', 
         JobOfferListCreateAPIView.as_view(),
         name='joboffer-list'),

    path('jobs/<int:pk>/',
         JobOfferDetailAPIView.as_view(),
         name='joboffer-detail')
]
