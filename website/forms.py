import os
from django import forms
from .models import members, Newmember, member_type, payment_choice
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import loader



class DoaMemberForm(forms.Form):
    membertype = forms.ChoiceField(label='', required=True, widget=forms.Select(attrs={'class':'col-md-6  inputsec membertype','placeholder': 'Select Member Type'}), choices=member_type, initial=' ')
 
    memberfees = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'readonly':'readonly','class':'col-md-6  inputsec memberfees' ,'placeholder': 'Amount'}), max_length=255)
    firstname = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={ 'class':'col-md-6  inputsec' ,'placeholder': 'Enter Name'}), max_length=100)
    email = forms.EmailField(label='', required=True,widget=forms.TextInput(attrs={ 'class':'col-md-6  inputsec' ,'placeholder': 'Enter Email'}), max_length=100)
    
    password = forms.CharField(required = True, label = '', widget = forms.PasswordInput(attrs = {'placeholder': 'Insert your password', 'class': 'col-md-6  inputsec password'}))
    re_password = forms.CharField(required = True, label = '', widget = forms.PasswordInput(attrs = {'placeholder': 'Re Insert the password', 'class': 'col-md-6  inputsec re_password'}))

    postaddress = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Enter Postal Address'}), max_length=255)
    peraddress = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Enter Permanent Address'}), max_length=255)
    
    state = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-6 inputsec' ,'placeholder': 'State'}))
    pincode = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-6 inputsec' ,'placeholder': 'Pincode'}))
    study = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Education'}))
    institute = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Institute Name'}))
    interest = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Interested Area'}))
    extrainterest = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Extra Activities'}))
    hospital = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Working In Hospital / Clinic'}))
    position = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Position'}))
    clinicaddress = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Clinic Address'}))
    contactno = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-6 inputsec' ,'placeholder': 'Contact no.'}))
    mobile = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'col-md-6 inputsec' ,'placeholder': 'Mobile no.'}))
    paymenttype = forms.CharField(label='Payment Type', required=True, widget=forms.RadioSelect(attrs={'class':'typesec inputsec1'}, choices = payment_choice))
    paymentscreen = forms.FileField(help_text = '', required = True, label = 'Payment Screen')
    degreescreen = forms.FileField(help_text = '', required = False, label = 'Degree Image')
    certificatescreen = forms.FileField(help_text = '', required = False, label = 'Certificate Image')
    memberimage = forms.FileField(help_text = '', required = False, label = 'Member Image')

    def __init__(self, *args, **kwargs):
        super(DoaMemberForm, self).__init__(*args, **kwargs)
        self.fields['paymentscreen'].widget.attrs['class'] = 'form-control inputsec1'
        self.fields['degreescreen'].widget.attrs['class'] = 'form-control inputsec1'
        self.fields['certificatescreen'].widget.attrs['class'] = 'form-control inputsec1'
        self.fields['memberimage'].widget.attrs['class'] = 'form-control inputsec1'


    def clean_email(self):
        email = self.cleaned_data['email']
        users_found = User.objects.filter(email__iexact = email)
        self.email_already_exist = False
        if len(users_found) >= 1:
            self.email_already_exist = True
            raise forms.ValidationError('email already exist')
        return email

    def clean_phone(self):
        mobile = self.cleaned_data['mobile']
        if mobile:
            if members.objects.filter(mobile=mobile).exists():
                raise forms.ValidationError("Another user with this phone already exists")
        return mobile

    # def save(self):
    #     data = self.cleaned_data
    #     mdata = members(membertype = data['membertype'], memberfees = data['memberfees'], firstname=data['firstname'], email=data['email'], postaddress=data['postaddress'], peraddress=data['peraddress'], state=data['state'], pincode=data['pincode'],    study=data['study'], institute=data['institute'], interest=data['interest'], extrainterest=data['extrainterest'], hospital=data['hospital'], position=data['position'], clinicaddress=data['clinicaddress'], contactno=data['contactno'], mobile=data['mobile'], paymenttype=data['paymenttype'], paymentscreen=request.FILES['paymentscreen'], degreescreen=request.FILES['degreescreen'], certificatecreen=request.FILES['certificatescreen'])
    #     mdata.save()
    #     return True

class UpdateDoaMemberForm(forms.Form):
    username = forms.CharField(widget= forms.HiddenInput(), required= False)
    postaddress = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Enter Postal Address'}), max_length=255)
    peraddress = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Enter Permanent Address'}), max_length=255)
    
    state = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-6 inputsec' ,'placeholder': 'State'}))
    pincode = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-6 inputsec' ,'placeholder': 'Pincode'}))
    study = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Education'}))
    institute = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Institute Name'}))
    interest = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Interested Area'}))
    extrainterest = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Extra Activities'}))
    hospital = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Working In Hospital / Clinic'}))
    position = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Position'}))
    clinicaddress = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'col-md-12 inputsec1' ,'placeholder': 'Clinic Address'}))
    # degreescreen = forms.FileField(help_text = '', required = False, label = 'Degree Image')
    # certificatescreen = forms.FileField(help_text = '', required = False, label = 'Certificate Image')
    # memberimage = forms.FileField(help_text = '', required = False, label = 'Member Image')

    # def __init__(self, *args, **kwargs):
    #     super(UpdateDoaMemberForm, self).__init__(*args, **kwargs)
    #     self.fields['degreescreen'].widget.attrs['class'] = 'form-control inputsec1'
    #     self.fields['certificatescreen'].widget.attrs['class'] = 'form-control inputsec1'
    #     self.fields['memberimage'].widget.attrs['class'] = 'form-control inputsec1'

    # def update(self):
    #     data = self.cleaned_data
    #     info = members.objects.filter(user = data['username'])                 #getting the user id
    #     if info:                                                            #if personal Id exist use update
    #         info = info[0]
    #         if info:
    #             info.postaddress = data['postaddress']
    #             info.peraddress = data['peraddress']
    #             info.state = data['state']
    #             info.pincode = data['pincode']
    #             info.study = data['study']
    #             info.institute = data['institute']
    #             info.interest = data['interest']
    #             info.extrainterest = data['extrainterest']
    #             info.hospital = data['hospital']
    #             info.position = data['position']
    #             info.clinicaddress = data['clinicaddress']
    #             # info.paymentscreen = files['paymentscreen']
    #             # info.degreescreen = files['degreescreen']
    #             # info.certificatescreen = files['certificatescreen']
    #             # info.memberimage = files['memberimage']
    #             info.save()

class UpdateDoaMemberImageForm(forms.Form):
    username = forms.CharField(widget= forms.HiddenInput(), required= False)
    memberimage = forms.FileField(help_text = '', required = False, label = 'Member Image')

    def __init__(self, *args, **kwargs):
        super(UpdateDoaMemberImageForm, self).__init__(*args, **kwargs)
        self.fields['memberimage'].widget.attrs['class'] = 'form-control inputsec1'

class UpdateDoaMemberCertificateForm(forms.Form):
    username = forms.CharField(widget= forms.HiddenInput(), required= False)
    certificatescreen = forms.FileField(help_text = '', required = False, label = 'Certificate Image')

    def __init__(self, *args, **kwargs):
        super(UpdateDoaMemberCertificateForm, self).__init__(*args, **kwargs)
        self.fields['certificatescreen'].widget.attrs['class'] = 'form-control inputsec1'

class UpdateDoaMemberDegreeForm(forms.Form):
    username = forms.CharField(widget= forms.HiddenInput(), required= False)
    degreescreen = forms.FileField(help_text = '', required = False, label = 'Degree Image')

    def __init__(self, *args, **kwargs):
        super(UpdateDoaMemberDegreeForm, self).__init__(*args, **kwargs)
        self.fields['degreescreen'].widget.attrs['class'] = 'form-control inputsec1'
