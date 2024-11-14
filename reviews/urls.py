from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("all-reviews", views.AllReviews.as_view()),
    path("reviews/<int:id>", views.ReviewDetails.as_view())
]
