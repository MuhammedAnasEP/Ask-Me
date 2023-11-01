from django.forms import ModelForm
from posts.models import CustomUser


class ProfileForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','username','bio','location')