from django import forms
from .models import Member
from django.utils.translation import ugettext_lazy as _


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = '__all__'  # ( 'itf_id', 'first_name', 'last_name', 'birthdate', 'sex', 'level', 'team',)