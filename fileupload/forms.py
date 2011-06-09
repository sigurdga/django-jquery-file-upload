from django.forms import ModelForm
from fileupload.models import Picture

class PictureForm(ModelForm):

    class Meta:
        model = Picture

