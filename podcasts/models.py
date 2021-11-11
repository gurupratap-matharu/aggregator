"""Database models for the aggregator app"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class ActiveManager(models.Manager):

    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)


class Episode(models.Model):
    """Data model for a Podcasts' episode"""

    title = models.CharField(verbose_name=_("Title"), max_length=200)
    description = models.TextField(verbose_name=_("Description"))
    pub_date = models.DateTimeField(verbose_name=_("Publication Date"))
    link = models.URLField(verbose_name=_("Url"))
    image = models.URLField(verbose_name=_("Image"))
    podcast_name = models.CharField(
        verbose_name=_("Podcast Name"), max_length=100)
    guid = models.CharField(verbose_name=_("Guid"), max_length=200)
    active = models.BooleanField(verbose_name=_("Active"), default=True)
    featured = models.BooleanField(verbose_name=_("Featured"), default=False)

    objects = ActiveManager()

    class Meta:
        verbose_name = _('Episode')
        verbose_name_plural = _('Episodes')
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"
