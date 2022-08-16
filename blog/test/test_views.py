from django.http import response
from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.urls import reverse

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog_home = reverse('blog-home')
        self.blog_home = reverse('blog-about')
        self.post_detail = reverse('post-detail',  kwargs={'pk':1})
        self.post_create = reverse('post-create')
        #self.user = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
        # self.post1= Post.objects.create(
        #     id = 1,
        #     title = "post1",
        #     content = "The post",
        #     author = self.user
        # )

    # def test_postlist_Get(self):
    #     #setup
    #     #test
    #     #assertions
    #     response = self.client.get(self.blog_home)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/home.html,',  'blog/base.html')

    # def test_postdetail_Get(self):
    #     response = self.client.get(reverse(self.post_detail))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/post_detail.html')

    # def test_postcreate_Get(self):
    #     response = self.client.get(reverse(self.post_create))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/post_form.html')

    # def test_about_Get(self):
    #     response = self.client.get(self.blog_about)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/about.html')



    

