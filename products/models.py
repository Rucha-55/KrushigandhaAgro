from django.db import models
from tinymce.models import HTMLField

class Product(models.Model):
    title = models.CharField(max_length=255)
    # description = models.TextField()
    image = models.ImageField(upload_to='products/')  # Requires Pillow library
    features = HTMLField()  # Use TinyMCE for rich text editing

    def feature_list(self):
        # Extract features by splitting on newline (if plain text is used in the editor)
        return self.features.split('\n')

    def __str__(self):
        return self.title
