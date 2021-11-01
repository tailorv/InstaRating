from django.test import TestCase
from .models import Rate,Profile,Project,User

# Create your tests here.
class ProjectTestClass(TestCase):
    #setuo method
    def setUp(self):
        self.user = User(username='mune')
        self.mune = Project(title = 'football', url='https://www.skysports.com/football/news/11675/12456260/nuno-espirito-santo-tottenham-sack-head-coach', description = 'Tottenham manager', user = self.user, photo = 'default.png', date = '20-10-2021')
        
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mune,Project))
        
    def test_save_method(self):
        self.mune.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)    