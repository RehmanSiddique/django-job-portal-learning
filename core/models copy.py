"""
Models module for the pages app.

This module defines the database models for the CRUD application:
- Post: Main model for storing posts with name, title, description, and image
- NotesReview: One-to-many relationship for user reviews on posts
- NotesStore: Many-to-many relationship for storing multiple posts
- NoteCertificate: One-to-one relationship for post certificates
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model representing a blog post or note.
    
    Attributes:
        name (CharField): Name of the post author or post identifier
        title (CharField): Title of the post
        description (TextField): Detailed description or content of the post
        image (ImageField): Optional image associated with the post
        date_added (DateTimeField): Timestamp when the post was created
    """
    # Name field with max 100 characters, can be blank, defaults to empty string
    name = models.CharField(max_length=100, blank=True, default='')
    
    # Title field with max 200 characters, can be blank, defaults to empty string
    title = models.CharField(max_length=200, blank=True, default='')
    
    # Description field with max 500 characters, can be blank, defaults to empty string
    description = models.TextField(max_length=500, blank=True, default='')
    
    # Image field that uploads to 'images/' directory, optional (can be null or blank)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    # Automatically set to current time when post is created
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """Return string representation of the post (its name)."""
        return self.name


class NotesReview(models.Model):
    """
    NotesReview model representing user reviews for posts.
    
    Implements a one-to-many relationship where:
    - One User can write many reviews
    - One Post can have many reviews
    
    Attributes:
        user (ForeignKey): The user who wrote the review
        post (ForeignKey): The post being reviewed
        rating (IntegerField): Numeric rating given to the post
        review (TextField): Text content of the review
        date_added (DateTimeField): Timestamp when review was created
    """
    # Foreign key to User model, deletes all reviews if user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Foreign key to Post model, deletes all reviews if post is deleted
    # related_name allows accessing reviews from Post object: post.reviews.all()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    
    # Integer field for storing rating value
    rating = models.IntegerField()
    
    # Text field for review content, max 300 characters, can be blank
    review = models.TextField(max_length=300, blank=True, default='')
    
    # Automatically set to current time when review is created
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """Return string representation showing username, post title, and rating."""
        return f'{self.user.username} - {self.post.title} - {self.rating}'


class NotesStore(models.Model):
    """
    NotesStore model representing a store or collection of posts.
    
    Implements a many-to-many relationship where:
    - One store can have many posts
    - One post can belong to many stores
    
    Attributes:
        name (CharField): Name of the store
        location (CharField): Physical or virtual location of the store
        notes (ManyToManyField): Collection of posts in this store
    """
    # Name of the store, max 100 characters, required field
    name = models.CharField(max_length=100)
    
    # Location of the store, max 100 characters, required field
    location = models.CharField(max_length=100)
    
    # Many-to-many relationship with Post model
    # related_name allows accessing stores from Post object: post.note_store.all()
    notes = models.ManyToManyField(Post, related_name='note_store')
    
    def __str__(self):
        """Return string representation of the store (its name)."""
        return self.name


class NoteCertificate(models.Model):
    """
    NoteCertificate model representing a certificate for a post.
    
    Implements a one-to-one relationship where:
    - One post can have exactly one certificate
    - One certificate belongs to exactly one post
    
    Attributes:
        note (OneToOneField): The post this certificate is for
        certificate_name (CharField): Name of the certificate
        certificate_number (CharField): Unique certificate number
        issued_date (DateField): Date when certificate was issued
        valid_until (DateField): Optional expiration date of certificate
    """
    # One-to-one relationship with Post, deletes certificate if post is deleted
    # related_name allows accessing certificate from Post: post.certificate
    note = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='certificate')
    
    # Name of the certificate, max 100 characters
    certificate_name = models.CharField(max_length=100)
    
    # Unique certificate number, max 100 characters
    certificate_number = models.CharField(max_length=100)
    
    # Date when certificate was issued, defaults to current date
    issued_date = models.DateField(default=timezone.now)
    
    # Optional expiration date for the certificate
    valid_until = models.DateField(null=True, blank=True)
    
    def __str__(self):
        """Return string representation showing certificate name and post title."""
        return f'{self.certificate_name} - {self.note.title}'