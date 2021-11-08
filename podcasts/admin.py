from django.contrib import admin

from podcasts.models import Episode


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date", "active", "featured")
    list_filter = ("active", "featured")
    list_editable = ("active", "featured")
    search_fields = ("podcast_name", "title")
    date_hierarcy = "pub_date"
    ordering = ("-pub_date",)
