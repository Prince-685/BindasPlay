from django.db import models
from django.forms import ModelForm

class Text(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = '__all__'