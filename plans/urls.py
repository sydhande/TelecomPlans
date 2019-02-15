from django.urls import path
from django_filters.views import FilterView
from . filters import LandlineFilter, BroadbandFilter
from . import views
from .views import (
    LandlineListView, 
    LandlineDetailView,
    LandlineCreateView,
    LandlineUpdateView,
    LandlineDeleteView,
    BroadbandListView, 
    BroadbandDetailView,
    BroadbandCreateView,
    BroadbandUpdateView,
    BroadbandDeleteView,
)


urlpatterns = [
    path('landline/<int:pk>/', LandlineDetailView.as_view(), name='landline-detail'),
    path('landline/<int:pk>/update', LandlineUpdateView.as_view(), name='landline-update'),
    path('landline/<int:pk>/delete', LandlineDeleteView.as_view(), name='landline-delete'),
    path('landline/new/', LandlineCreateView.as_view(), name='landline-create'),
    path('about/', views.about, name='plans-about'),
    path('', FilterView.as_view(filterset_class=LandlineFilter,  template_name='plans/home.html'), name='plans-home'),
    path('broadband/<int:pk>/', BroadbandDetailView.as_view(), name='broadband-detail'),
    path('broadband/<int:pk>/update', BroadbandUpdateView.as_view(), name='broadband-update'),
    path('broadband/<int:pk>/delete', BroadbandDeleteView.as_view(), name='broadband-delete'),
    path('broadband/', FilterView.as_view(filterset_class=BroadbandFilter,  template_name='plans/bbhome.html'), name='plans-bbhome'),
    path('broadband/new/', BroadbandCreateView.as_view(), name='broadband-create'),
]

# path('search/', FilterView.as_view(filterset_class=LandlineFilter, template_name='plans/landline_list.html'), name='landline-search')
#path('',  LandlineListView.as_view(), name='plans-home'),
