from django.test import TestCase,Client
from django.urls import reverse
from .apiviews import PollList
from.models import Poll,User
from datetime import datetime

# Create your tests here.

#poll test

class PollViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test',password='test')
        self.client.force_login(self.user)
        self.poll = Poll.objects.create(title='test poll',description='test poll',pub_date=datetime.now())
    def is_poll_exist(self):
        response = self.client.get(reverse('polls:poll-detail',kwargs={'pk':self.poll.pk}))
        self.assertEqual(response.status_code,200)
    def test_create_poll_with_missing_data(self):
        response = self.client.post(reverse('polls:poll-list'))
        self.assertEqual(response.status_code,400)
    
    def test_create_invalid_poll(self):
        response = self.client.post(reverse('polls:poll-list'),{'title':'test poll','description':'test poll','pub_date':datetime.now()})
        self.assertEqual(response.status_code,400)
        

