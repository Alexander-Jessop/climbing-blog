'''
Modles for blog app
'''
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Topic(models.Model):
    '''
    Represents a topic for blog posts.

    Attributes:
        name (TextField): The name of the topic. Must be unique.
        slug (SlugField): URL-friendly version of the topic name. Also unique.

    Methods:
        str: Overrides the default str method to return the topic name.
        save: Overrides the default save method to add slug generation.
    '''

    name = models.TextField(unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **keyargs):
        self.slug = slugify(self.name)
        super().save(*args, **keyargs)

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'slug': self.slug})


class Post(models.Model):
    '''
    Represents a blog post.

    Attributes:
        DRAFT (str): Constant indicating a post's status as 'draft'.
        PUBLISHED (str): Constant indicating a post's status as 'published'.
        STATUS_CHOICES (list): Choices for the status of the post.
        title (TextField): The title of the post.
        content (TextField): The main content of the post.
        author (ForeignKey): The user who authored the post.
        created (DateTimeField): Timestamp indicating when the post was created.
        updated (DateTimeField): Timestamp indicating the last time the post was updated.
        status (TextField): Indicates whether the post is a draft or published.
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

    title = models.TextField(null=False, blank=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICES, default=DRAFT)
    published = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **keyargs):
        self.slug = slugify(self.title)
        if self.status == self.PUBLISHED and not self.published:
            self.published = timezone.now()
        super().save(*args, **keyargs)


class Comment(models.Model):
    '''
    Represents a comment on a blog post.

    Attributes:
        post (ForeignKey): Relationship to the Post model. Comments are related to posts.
        name (CharField): Name of the commenter.
        email (EmailField): Email address of the commenter.
        text (TextField): The content of the comment.
        approved (BooleanField): Indicates if the comment is approved for display.
        created (DateTimeField): Timestamp when the comment was created.
        updated (DateTimeField): Timestamp when the comment was last updated.

    Methods:
        __str__: Returns a readable string representation of the comment.
    '''

    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    text = models.TextField(max_length=200, null=False, blank=False)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

    class Meta:
        '''
        Meta configuration for the Comment model.

        Attributes:
            ordering (list): Sets the default order for comments based on the 'created'
            timestamp in reverse order.
        '''
        ordering = ['-created']


class PhotoSubmission(models.Model):
    '''
    Represents a photo submission for the photo contest.

    Attributes:
        name (CharField): The name of the user submitting the photo.
        email (EmailField): Email address of the user submitting the photo.
        image (ImageField): The image file that the user submits.
        submitted_at (DateTimeField): Timestamp indicating when the photo was submitted.

    Methods:
        __str__: Returns a readable string representation of the submission.
    '''

    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    image = models.ImageField(upload_to='photo_submissions/')
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Photo Submission by {self.name} on {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
