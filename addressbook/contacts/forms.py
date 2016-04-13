from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from contacts.models import (
    Contact,
    Address,
)


#class ContactForm(forms.ModelForm):
#    #test= forms.BooleanField()
#    #confirm_email = forms.EmailField(
#    #    label="Confirm email",
#    #    required=True,
#    #)
#
#    class Meta:
#        model = Contact
#
#    def __init__(self, *args, **kwargs):
#
#        if kwargs.get('instance'):
#            email = kwargs['instance'].email
#            kwargs.setdefault('initial', {})['confirm_email'] = email
#
#        return super(ContactForm, self).__init__(*args, **kwargs)
#
#    def clean(self):
#
#        if (self.cleaned_data.get('email') !=
#            self.cleaned_data.get('confirm_email')):
#
#            raise ValidationError(
#                "Email addresses must match."
#            )
#        if (len(self.cleaned_data.get('first_name')) > 10):
#            raise ValidationError(
#                "Only 10 char."
#            )
#        
#
#        return self.cleaned_data


# inlineformset_factory creates a Class from a parent model (Contact)
# to a child model (Address)
#ContactAddressFormSet = inlineformset_factory(
#    Contact,
#    Address,
#)