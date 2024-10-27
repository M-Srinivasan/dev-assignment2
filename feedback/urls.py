from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
    path('feedbacks/', views.view_feedbacks, name='view_feedbacks'),  # New URL pattern
]
