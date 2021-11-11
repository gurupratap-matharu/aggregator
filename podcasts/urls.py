from django.urls import path

from podcasts.views import HomePageView, SearchResultsListView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
