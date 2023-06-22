from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidatesView.as_view(),
    name='candidate')
   
]
