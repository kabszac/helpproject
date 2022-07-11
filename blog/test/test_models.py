from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User

class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
        self.post2= Post.objects.create(
            title = "post2",
            content = "The post",
            author = self.user
        )
        self.comment1 = Comment.objects.create(
            post = self.post2,
            name = self.user,
            content = "A great post"
        )

    def test_postmodel(self):
        self.assertEqual(self.post2.title, 'post2')
        self.assertEqual(self.post2.content, 'The post')
        self.assertEqual(self.post2.author, self.user)

    def test_commentmodel(self):
        self.assertEqual(self.comment1.post, self.post2)
        self.assertEqual(self.comment1.content, 'A great post')
        self.assertEqual(self.comment1.name, self.user)


