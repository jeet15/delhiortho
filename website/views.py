from django.template.defaultfilters import date
import datetime
import random
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from django.views.generic import ListView, DetailView, CreateView
from .models import Officebearers, Pastofficebearers, Pastmembers, Doanews, Doaevents, Archivejournal, Awards, members, Newmember,Eposter,Homeslider
from .forms import DoaMemberForm, UpdateDoaMemberForm, UpdateDoaMemberImageForm, UpdateDoaMemberDegreeForm, UpdateDoaMemberCertificateForm

from django.http import HttpResponseRedirect

class HomeView(ListView):
    template_name = 'home.html'
    queryset = Officebearers.objects.all()
    queryset4 = Homeslider.objects.all()
    this_month = datetime.datetime.now()
    new_month = this_month.strftime("%B")
    this_year = this_month.year
    print(new_month)
    queryset1 = Doaevents.objects.filter(emonth=new_month)
    queryset2 = Doanews.objects.filter(year = this_year)

    def get_context_data(self, **kwargs):
    	
        context = super(HomeView, self).get_context_data(**kwargs)
        context['event'] = self.queryset1
        context['post'] = self.queryset
        context['news'] = self.queryset2
        context['slider'] = self.queryset4
        return context


def doa_member(request):
    if request.method == 'POST':
        activation_code = str(int(random.random()*100000))
        form = DoaMemberForm(request.POST, request.FILES)
        if form.is_valid():
            memberid = 'TM'+activation_code
            membertype = request.POST.get('membertype')
            memberfees = request.POST.get('memberfees')
            firstname = request.POST.get('firstname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            postaddress = request.POST.get('postaddress')
            peraddress = request.POST.get('peraddress')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            study = request.POST.get('study')
            institute = request.POST.get('institute')
            interest = request.POST.get('interest')
            extrainterest = request.POST.get('extrainterest')
            hospital = request.POST.get('hospital')
            position = request.POST.get('position')
            clinicaddress = request.POST.get('clinicaddress')
            contactno = request.POST.get('contactno')
            mobile = request.POST.get('mobile')
            paymenttype = request.POST.get('paymenttype')
            paymentscreen = request.FILES.get('paymentscreen')
            degreescreen = request.FILES.get('degreescreen')
            certificatescreen = request.FILES.get('certificatescreen')
            memberimage = request.FILES.get('memberimage')

            user = User.objects.create_user(username = memberid, password=password, email=email, first_name=firstname,)
            mdata = members(membertype = membertype, memberfees = memberfees,  firstname=firstname  ,email=email, postaddress=postaddress, peraddress=peraddress, state=state, pincode=pincode, study=study, institute=institute, interest=interest, extrainterest=extrainterest, hospital=hospital, position=position, clinicaddress=clinicaddress, contactno=contactno, mobile=mobile, paymenttype=paymenttype, paymentscreen=paymentscreen, degreescreen=degreescreen, certificatescreen=certificatescreen, status = 2, user=memberid)
            user.save()
            mdata.save()

            #send_mail(subject, message, from_email, to_list, fail_silently=True)
            subject = 'DOA Membership Registration'
            message = 'Thankyou for the online regsitration at Delhi Orthopedic Association.\n We have received your request becomeing the DOA Member.\nYour document verification is under process, we will mail you once they verified.\n \n \nWarm Regards\n Delhi Orthopedic Association' 
            from_email = settings.EMAIL_HOST_USER
            to_list = [mdata.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)
            # form.save()
            return redirect('member-login.html')
        else:
            print(form.errors)
    else:
        form = DoaMemberForm()
        
    return render(request, 'member-registration.html', {'form': form})

def member_login(request):

    if request.method == 'POST':
        username = request.POST['userid']
        # email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # loginuser = User.objects.filter(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('member-area.html')
        # user = auth.authenticate
        else:
            error = 'Wrong Credentials'
            return render(request, 'member-login.html', {'error': error})
    else:
        return render(request, 'member-login.html', {})



def member_area(request):
    if not request.user.is_authenticated:
            return redirect('member-login.html')
    else:
        return render(request, 'member-area.html')

def member_profile(request, username):
    if not request.user.is_authenticated:
            return redirect('/member-login.html')
    else:
        member = members.objects.filter(user = username)    
        return render(request, 'member-profile.html', {'member':member})


def edit_member_profile(request, username):
    if not request.user.is_authenticated:
            return redirect('/member-login.html')
    else:
        if request.method == 'POST':
            data = request.POST
            if data:
                form = UpdateDoaMemberForm(data)
                if form.is_valid():
                    info = members.objects.filter(user = data['username'])
                    if info:
                        info = info[0]
                        info.postaddress = data['postaddress']
                        info.peraddress = data['peraddress']
                        info.state = data['state']
                        info.pincode = data['pincode']
                        info.study = data['study']
                        info.institute = data['institute']
                        info.interest = data['interest']
                        info.extrainterest = data['extrainterest']
                        info.hospital = data['hospital']
                        info.position = data['position']
                        info.clinicaddress = data['clinicaddress']
                        info.save()

                    member = members.objects.filter(user = username)    
                return render(request, 'member-profile.html', {'member':member})
            else:
                member = members.objects.filter(user = username)
                return render(request, 'edit-member-profile.html', {'form': form, 'member':member})

            # print("data not updated")
        else:
            info = members.objects.filter(user = username)
            if info:
                info = info[0]
                form =  UpdateDoaMemberForm({
                        'username':info.user,
                        'postaddress':info.postaddress,
                        'peraddress':info.peraddress,
                        'state':info.state,
                        'pincode': info.pincode,
                        'study': info.study,
                        'institute':info.institute,
                        'interest':info.interest,
                        'extrainterest':info.extrainterest,
                        'hospital':info.hospital,
                        'position':info.position,
                        'clinicaddress':info.clinicaddress
                        }) 
                imageform= UpdateDoaMemberImageForm()  
                degreeform= UpdateDoaMemberDegreeForm()  
                certificateform= UpdateDoaMemberCertificateForm()  
            member = members.objects.filter(user = username)
        return render(request, 'edit-member-profile.html', {'form': form, 'member':member, 'imageform':imageform, 'certificateform':certificateform, 'degreeform':degreeform})

def edit_member_image(request, username):
    if not request.user.is_authenticated:
            return redirect('/member-login.html')
    else:
        if request.method == 'POST':
            data = request.FILES
            form = UpdateDoaMemberImageForm(data)
            if form.is_valid():
                info = members.objects.filter(user = username)
                if info:
                    info = info[0]
                    info.member_image = data['memberimage']
                    info.save()
                member = members.objects.filter(user = username)    
            return render(request, 'member-profile.html', {'member':member})
        else:
            imageform= UpdateDoaMemberImageForm()  
            degreeform= UpdateDoaMemberDegreeForm()  
            certificateform= UpdateDoaMemberCertificateForm()  
            member = members.objects.filter(user = username)
        return render(request, 'edit-member-profile.html', {'form': form, 'member':member, 'imageform':imageform, 'certificateform':certificateform, 'degreeform':degreeform})
            # member = members.objects.filter(user = username)
            # return render(request, 'edit-member-profile.html', {'form': form, 'member':member, 'imageform':imageform})

def edit_member_degree(request, username):
    if not request.user.is_authenticated:
            return redirect('/member-login.html')
    else:
        if request.method == 'POST':
            data = request.FILES
            form = UpdateDoaMemberDegreeForm(data)
            if form.is_valid():
                info = members.objects.filter(user = username)
                if info:
                    info = info[0]
                    info.degreescreen = data['degreescreen']
                    info.save()
                member = members.objects.filter(user = username)    
            return render(request, 'member-profile.html', {'member':member})
        else:
            imageform= UpdateDoaMemberImageForm()  
            degreeform= UpdateDoaMemberDegreeForm()  
            certificateform= UpdateDoaMemberCertificateForm()  
            member = members.objects.filter(user = username)
            return render(request, 'edit-member-profile.html', {'form': form, 'member':member, 'imageform':imageform, 'certificateform':certificateform, 'degreeform':degreeform})

def edit_member_certificate(request, username):
    if not request.user.is_authenticated:
            return redirect('/member-login.html')
    else:
        if request.method == 'POST':
            data = request.FILES
            form = UpdateDoaMemberCertificateForm(data)
            if form.is_valid():
                info = members.objects.filter(user = username)
                if info:
                    info = info[0]
                    info.certificatescreen = data['certificatescreen']
                    info.save()
                member = members.objects.filter(user = username)    
            return render(request, 'member-profile.html', {'member':member})
        else:
            imageform= UpdateDoaMemberImageForm()  
            degreeform= UpdateDoaMemberDegreeForm()  
            certificateform= UpdateDoaMemberCertificateForm()  
            member = members.objects.filter(user = username)
            return render(request, 'edit-member-profile.html', {'form': form, 'member':member, 'imageform':imageform, 'certificateform':certificateform, 'degreeform':degreeform})

def member_list(request):
    member = members.objects.all()
    print(member)
    return render(request, 'member-list.html', {'member':member})

class EventView(ListView):
	model = Doaevents
	template_name = 'doa-events.html'


class EventDetailView(DetailView):
	# model = Doaevents
	queryset = Doaevents.objects.all()
	template_name = 'detail_list.html'
	def get_context_data(self, *args,**kwargs):
		print(self.kwargs)
		context = super(EventDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context


def president_message(request):
	return render(request, 'president-message.html', {})


def secretary_message(request):
	return render(request, 'secretary-message.html', {})


class PastOfficebearersView(ListView):
	model = Pastofficebearers
	template_name = 'office-bearers-2018-19.html'


class OfficebearersView(ListView):
	model = Officebearers
	template_name = 'office-bearers-2019-20.html'


def doaelections2019_2020(request):
	return render(request, 'doa-elections-2019-2020.html', {})


class PastpresidentView(ListView):
	model = Pastmembers
	template_name = 'past-presidents-and-secretaries.html'


class DoanewsView(ListView):
	model = Doanews
	template_name = 'doa-news.html'



class DoaAllEventView(ListView):
	model = Doaevents
	template_name = 'doa-events.html'




def archived_events(request):
	return render(request, 'archived-events.html', {})


def doa_fellowship(request):
	return render(request, 'doa-fellowship.html', {})


class DoaawardsView(ListView):
	model = Awards
	template_name = 'doacon-award-2019.html'


def doa_journal(request):
	return render(request, 'doa-journal.html', {})


def archive():
	return render(request, 'archive.html', {})



def doa_journal_archive(request):
	return render(request, 'doa-journal-archive.html', {})

def member_registration(request):
	return render(request, 'member-registration.html', {})


def subspeciality(request):
	return render(request, 'subspeciality.html', {})


def photo_gallery(request):
	return render(request, 'photo-gallery.html', {})



def covid(request):
	return render(request, 'covid_19.html', {})


class EposterView(ListView):
	model = Eposter
	template_name = 'eposter.html'





def contact(request):
	return render(request, 'contact.html', {})


def contact_us(request):
    form = DoaMemberForm()
    return render(request, 'member-registration.html', {'form': form})