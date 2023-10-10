'''
Modles for blog app
'''
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    '''
    Represents a topic for blog posts.

    Attributes:
        name (CharField): The name of the topic. Must be unique.
        slug (SlugField): URL-friendly version of the topic name. Also unique.

    Methods:
        str: Overrides the default str method to return the topic name.
        save: Overrides the default save method to add slug generation.
    '''
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **keyargs):
        self.slug = slugify(self.name)
        super().save(*args, **keyargs)


class Post(models.Model):
    '''
    Represents a blog post.

    Attributes:
        DRAFT (str): Constant indicating a post's status as 'draft'.
        PUBLISHED (str): Constant indicating a post's status as 'published'.
        STATUS_CHOICES (list): Choices for the status of the post.
        title (CharField): The title of the post.
        content (TextField): The main content of the post.
        author (ForeignKey): The user who authored the post.
        created (DateTimeField): Timestamp indicating when the post was created.
        updated (DateTimeField): Timestamp indicating the last time the post was updated.
        status (CharField): Indicates whether the post is a draft or published.
        published (DateTimeField): Timestamp indicating when the post was published.
        slug (SlugField): URL-friendly version of the post title.
        topics (ManyToManyField): Topics associated with the post.

    Methods:
        save: Overrides the default save method to add slug generation and set published date.
    '''
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    title = models.TextField(max_length=50, null=False, blank=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    published = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    topics = models.ManyToManyField(Topic, blank=True)

    def save(self, *args, **keyargs):
        self.slug = slugify(self.title)
        if self.status == self.PUBLISHED and not self.published:
            self.published = timezone.now()
        super().save(*args, **keyargs)
