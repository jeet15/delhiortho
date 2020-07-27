# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User

from .models import ContactUs
from .forms import ContactInfoForm

class ContactPage(object):
    def get_contact(self):
        form = ContactInfoForm()
        return {'form':form}

    def post_contact(self, data={}):
        if data:
            form = ContactInfoForm(data)
            if form.is_valid():
                form.save()
                return {'status': 1, 'message':'Your message sent  successfully'}
            else:
                return{'status': 0, 'message':'Please Fill the captche correctly'}
        form = ContactInfoForm()
        return{'form':form}       
