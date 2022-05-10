from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
                    username='testuser1', password='abc123')
        testuser1.save()

        # create a category
        testcategory = Category.objects.create(name='category1')     
        testcategory.save()

        # Create a blog post
        test_post = Post.published.create(
                        author=testuser1, title='This is a test title', body='Body content ayee', category=testcategory, status='published')
        test_post.save()

    def test_category_content(self):
        category = Category.objects.get(id=1)
        name = f'{category.name}'

        self.assertEqual(name, 'category1')


    def test_blog_content(self):

        post   = Post.published.get(id=1)
        author = f'{post.author}'
        title  = f'{post.title}'
        body   = f'{post.body}'
        status = f'{post.status}'
        categry= f'{post.category}' 

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'This is a test title')
        self.assertEqual(body, 'Body content ayee')
        self.assertEqual(status, 'published')
        self.assertEqual(categry, 'category1')
       