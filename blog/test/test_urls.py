from django.http import response
from django.test import SimpleTestCase
from blog.views import (PostListView, PostDetailView, PostCreateView,
 PostUpdateView, PostDeleteView, CommentCreateView, about, home
)
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
    def test_postlisturl(self):
        url = reverse('blog-home')
        self.assertEqual(resolve(url).func.view_class, PostListView )

    def test_abouturl(self):
        url = reverse('blog-about')
        self.assertEqual(resolve(url).func, about)

    def test_postdetailurl(self):
        url = reverse('post-detail', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView )

    def test_postcreateurl(self):
        url = reverse('post-create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView )

    def test_postupdateurl(self):
        url = reverse('post-update', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, PostUpdateView )

    def test_postdeleteurl(self):
        url = reverse('post-delete', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, PostDeleteView)

    def test_commentcreteeurl(self):
        url = reverse('add-comment', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, CommentCreateView)