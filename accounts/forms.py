from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea
from .models import Account


class MySignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'email']



    @atomic
    def save(self, commit=True):
        # self.instance.is_active = False
        result = super().save(commit)
        profile = Account(user=result)
        if commit:
            profile.save()
        return result
