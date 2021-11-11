from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from podcasts.models import Episode


class HomePageTests(TestCase):

    def setUp(self):
        self.episode = Episode.objects.create(
            title="My awesome podcast episode",
            description="look mom, I made it!",
            pub_date=timezone.now(),
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
            podcast_name="My Python Podcast",
            guid="e7c1eb40-2e77-41e7-862b-a583eb19471a")

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_renders_correct_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'podcasts/homepage.html')

    def test_home_page_list_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'My awesome podcast episode')
