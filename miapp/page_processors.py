from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from django.utils import timezone
from .models import Author
from mezzanine.core.fields import RichTextField


class AuthorForm(forms.Form):
    name = forms.CharField()
    texto = RichTextField().formfield()
    #email = forms.EmailField()


@processor_for(Author)
def author_form(request, page):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            # Form processing goes here.

            nombre = form.data.get("name")
            texto = form.data.get("texto")
            newpage = Author.objects.create(title=nombre, dob=texto)
            newpage.set_parent(page)
            page.save()

            #print(newpage.get_absolute_url())
            redirect = request.path + "?submitted=true"
            return HttpResponseRedirect(redirect)
    return {"form": form}
