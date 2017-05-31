from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.

class Author(Page):
    #dob = models.DateField("Date")
    dob = RichTextField()

class Book(models.Model):
    author = models.ForeignKey("Author")
    #text = RichTextField(null=True)
    #cover = models.ImageField(upload_to="authors")
