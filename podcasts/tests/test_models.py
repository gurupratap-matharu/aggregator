from django.test import TestCase
from django.utils import timezone
from podcasts.models import Episode


class EpisodeTests(TestCase):

    def setUp(self):
        self.episode = Episode.objects.create(
            title="My awesome podcast episode",
            description="look mom, I made it!",
            pub_date=timezone.now(),
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
            podcast_name="My Python Podcast",
            guid="e7c1eb40-2e77-41e7-862b-a583eb19471a")

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "look mom, I made it!")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(self.episode.guid, "e7c1eb40-2e77-41e7-862b-a583eb19471a")

    def test_episode_str_representation(self):
        self.assertEqual(str(self.episode), "My Python Podcast: My awesome podcast episode")
