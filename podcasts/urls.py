from django.urls import path

from podcasts.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),]
