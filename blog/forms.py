"""
Module containing form definitions for the blog application.

Classes:
    PhotoSubmissionForm: Form for photo submission entries.
"""

from django import forms
from .models import PhotoSubmission


class PhotoSubmissionForm(forms.ModelForm):
    """
    A Django ModelForm for the PhotoSubmission model.

    This form inherits from forms.ModelForm and creates form fields for
    the 'name', 'email', and 'image' attributes of the PhotoSubmission model.

    Attributes:
        Meta: An inner class that provides metadata to the ModelForm class. 
              It tells the ModelForm which model to use and which fields to include.
    """

    class Meta:
        """Metadata options for the PhotoSubmissionForm."""
        model = PhotoSubmission
        fields = ['name', 'email', 'image']
