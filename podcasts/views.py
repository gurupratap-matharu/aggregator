import logging
from typing import Any, Dict

from django.db.models import Q, QuerySet
from django.views.generic import ListView

from podcasts.models import Episode

logger = logging.getLogger(__name__)


class HomePageView(ListView):
    """Renders the home page of the podcasts app."""

    template_name = 'podcasts/homepage.html'
    model = Episode
    paginate_by = 12

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.active().order_by('-featured')
        return context


class SearchResultsListView(ListView):
    model = Episode
    context_object_name = 'episodes'
    template_name = 'podcasts/homepage.html'
    paginage_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Episode.objects.active().filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
