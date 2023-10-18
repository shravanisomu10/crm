from django.contrib.auth.models import User
from django.test import  TestCase,Client
from django.urls import reverse

# Create your tests here.

class ViewTestCase(TestCase):
    def setup(self):
        self.client = Client()
        self.user_data = {
            'first_name': 'ram',
            'last_name':'pot',
            'email': 'rampot@,gmail.com',
            'username': 'ram2',
            'password': '123456'

        }
        self.user= User.object.create_user(**self.user_data)

    def test_can_view_login_page(self):
        response = self.client.get(reverse('register_view'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'register/registration.html')

    def test_user_can_register(self):
        self.user_data = {
           'first_name': 'ram',
            'last_name':'pot',
            'email': 'rampot@,gmail.com',
            'username': 'ram',
            'phone': '789456123',
            'address': 'drive',
            'password': '123456'
        }
        response = self.client.post(reverse('do_register'),self.user_data)
        self.assertEqual(response.status_code,302)
       # self.assertRedirect(response,reverse('register_view'))
        #created_user=User.object.get(username=self.user_data['username'])
        #self.assertEqual(created_user.first_name, self.user_data['first_name'])
        #self.assertEqual(created_user.last_name, self.user_data['last_name'])
        #self.assertEqual(created_user.email, self.user_data['email'])
        #self.assertEqual(created_user.phone, self.user_data['phone'])
        #self.assertEqual(created_user.address, self.user_data['address'])
        ##self.assertContains(response, 'Invalid username or password')
    
    def test_user_can_login(self):
        response = self.client.post(reverse('login'),{'username':'ram','password':'123456'})
        self.assertEqual(response.status_code,200)
        #self.assertRedirect(response,reverse('list'))


    def test_user_can_logout(self):
        self.client.login(username='ram', password='123456')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_delete_user(self):
        self.user_data = {
            'username': 'testuser6',
            'first_name':'name',
            'password': '56789',
            'last_name': 'Lastname',
            'email': 'testuser@example.com'
        }
        self.user = User.objects.create_user(username='testuser', password='12345')

        #response = self.client.post(reverse('delete_user', args=[self.user.id]))
       # self.assertEqual(response.status_code, 320)
       # self.assertRedirects(response, reverse('registration_data'))
        #self.assertFalse(User.objects.filter(id=self.user.id).exists())
        #self.client.login(username='testuser6',password='56789')
        #user_id=self.user.id
        url = reverse('delete_user', args=[self.user.id])
        response=self.client.post(url)
        self.assertEqual(response.status_code, 302) 
        #self.assertRedirects(response, reverse('registration_data'))
        self.assertFalse(User.objects.filter(username=self.user.username).exists())
        
    def test_update_user(self):

        new_data = {
            'first_name': 'Updated ram',
            'last_name': 'Updated pot',
            'email': 'rampot@gmail.com',
            'phone': '789456123',
            'address': 'drives',
            'password':'password',
            'username': 'ram2',
        }

        #print(new_data)
        self.user = User.objects.create_user(username='testuser', password='12345')
        print(self.user)
        
        response = self.client.post(reverse('update_user', args=[self.user.id]), new_data)
        #self.assertEqual(response.content, 302)
        #self.assertRedirects(response, reverse('registration_data'))
        self.user_update = User.objects.get(id=self.user.id)
        self.assertEqual(self.user_update.first_name, new_data['first_name'])
        self.assertEqual(self.user_update.last_name, new_data['last_name'])
        self.assertEqual(self.user_update.email, new_data['email'])

    def test_edit_user_view(self):
        self.user_data={
            'username':'testuser1',
            'last_name':'name',
            'password':'123456',
            'email':'testuser@gmail.com'
        }
        
        self.user= User.objects.create_user(username='testuser1',password='123456')
        self.client.login(username='testuser1', password='123456')
        user_id = self.user.id
        url = reverse('edit_user', args=[user_id])
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/edit_user.html')
        #print(response.content)
        self.assertContains(response, 'Address') 
        self.assertContains(response, "Email")
        #self.assertContains(response, self.user.last_name)
        #self.assertContains(response, self.user.password)
        #self.assertContains(response, self.user.email)
        