from django.urls import path
from .views.company import CompanyListView, CompanyDetailView
from .views.client import ClientListView, ClientDetailView
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
