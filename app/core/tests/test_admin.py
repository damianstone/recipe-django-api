from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSideTests(TestCase):

    # test than run before every test that we run
    def setUp(self):
        # login the user user
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='pass1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='pass1234',
            name='test user full name'
        )

    # test that users are listed on user page
    def test_users_listed(self):
        # create an url
        url = reverse('admin:core_user_changelist')
        # http request
        response = self.client.get(url)

        # check that the super user este bien creado
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
    

    def test_user_change_page(self):
        # create an url
        # /admin/core/user/1
        url = reverse('admin:core_user_change', args=[self.user.id])
        # http request
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        # create an url
        url = reverse('admin:core_user_add')
        # http request
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        
        
        
    