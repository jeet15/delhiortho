from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
member_type = ( ('','Select MemberType'), ('lifetime','Lifetime Member'), ('associate', 'Associate Member'))
payment_choice=(('NEFT','NEFT'), ('Cheque ','Cheque'), ('Cash Deposit','Cash Deposit'))

class Officebearers(models. Model):
	"""docstring for Officebearers"""

	name = models.CharField(max_length=200)
	email = models.CharField(max_length=250)
	phone = models.IntegerField(null=True)
	designation = models.CharField(max_length=250)
	image = models.FileField(upload_to = 'media')

	def __str__(self):
		return self.name + ' | ' + self.name


class Pastofficebearers(models. Model):
	"""docstring for Officebearers"""

	name = models.CharField(max_length=200)
	email = models.CharField(max_length=250)
	phone = models.IntegerField(null=True)
	designation = models.CharField(max_length=250)
	image = models.FileField(upload_to = 'pastmembers')

	def __str__(self):
		return self.name + ' | ' + self.name


class Pastmembers(models. Model):
	"""docstring for Officebearers"""

	year = models.IntegerField(null=True)
	president = models.CharField(max_length=200, null=True,  blank=True)
	secretary = models.CharField(max_length=200, null=True,  blank=True)
	treasurer = models.CharField(max_length=200, null=True,  blank=True)
	editor = models.CharField(max_length=200, null=True,  blank=True)
	annualmeet = models.CharField(max_length=200, null=True,  blank=True )

	def __str__(self):
		return self.president + ' | ' + self.president

class Doanews(models. Model):
	"""docstring for Officebearers"""

	title = models.CharField(max_length=200)
	year = models.IntegerField(null=True)
	description = models.TextField()
	newsfile = models.FileField(upload_to = 'doanews')

	def __str__(self):
		return self.title + ' | ' + self.title


class Doaevents(models. Model):
	"""docstring for Officebearers"""
	YEAR_CHOICES = (
    ('January','January'),
    ('Feburary', 'Feburary'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December'),
)

	title = models.CharField(max_length=200)
	category = models.CharField(max_length=150, default='upcoming')
	edate = models.IntegerField(null=True)
	emonth = models.CharField(max_length=20, choices=YEAR_CHOICES, null=True,)
	eyear = models.IntegerField(null=True)
	# description = models.TextField()
	description = RichTextField(blank=True, null=True)
	efile = models.FileField(null=True, blank=True ,upload_to = 'eventfile')

	def __str__(self):
		return self.title + ' | ' + self.title


class Archivejournal(models. Model):
	"""docstring for Officebearers"""

	title = models.CharField(max_length=200)
	year = models.IntegerField(null=True)
	description = models.TextField()
	archivefile = models.FileField(upload_to = 'archivejournal')

	def __str__(self):
		return self.title + ' | ' + self.year





class Awards(models. Model):
	"""docstring for Officebearers"""

	title = models.CharField(max_length=200)
	person = models.CharField(max_length=250)
	year = models.IntegerField(null=True)
	awardfile = models.FileField(upload_to = 'awards', null=True,  blank=True)

	def __str__(self):
		return self.title + ' | ' + self.person


class members(models.Model):
	MEMBER_TYPE = (
    ('lifetime','Lifetime Member'),
    ('associate', 'Associate Member'),
	)	
	PAYMENT_CHOICES=[('NEFT','NEFT'),
         ('Cheque ','select 2'), ('Cash Deposit','Cash Deposit')]
	# memberid = models.CharField(max_length=200)
	membertype = models.CharField(choices=MEMBER_TYPE, max_length=200)
	memberfees = models.IntegerField(null=True)
	firstname = models.CharField(max_length=255)
	email = models.CharField(max_length=255, null=True)
	# password = models.CharField(max_length=255)
	postaddress = models.CharField(max_length=555, null=True, blank=True)
	peraddress = models.CharField(max_length=555, null=True, blank=True)
	state = models.CharField(max_length=355, null=True, blank=True)
	pincode = models.IntegerField(null=True, blank=True)
	study = models.CharField(max_length=555, null=True, blank=True)
	institute = models.CharField(max_length=355, null=True, blank=True)
	interest = models.CharField(max_length=555, null=True, blank=True)
	extrainterest = models.CharField(max_length=355, null=True, blank=True)
	hospital = models.CharField(max_length=555, null=True, blank=True)
	position = models.CharField(max_length=255, null=True, blank=True)
	clinicaddress = models.CharField(max_length=555, null=True, blank=True)
	contactno = models.IntegerField(null=True, blank=True)
	mobile = models.IntegerField(null=True)
	paymenttype = models.CharField(choices=PAYMENT_CHOICES, max_length=200)
	paymentscreen = models.FileField(upload_to = 'members')
	degreescreen = models.FileField(upload_to = 'members', null=True, blank=True)
	certificatescreen = models.FileField(upload_to = 'members', null=True, blank=True)
	member_image = models.FileField(upload_to = 'members', null=True, blank=True)
	status =models.IntegerField(null=True)
	user = models.CharField(max_length=555, null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.membertype

	def get_absolute_url(self):
		print(self.id)
		return reverse('home')

class Oldmember(models.Model):
	membertype = models.CharField(max_length=255)
	memberfees = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	paymenttype = models.CharField(max_length=255)

	
class Newmember(models.Model):
	MEMBER_TYPE = (
    ('lifetime','Lifetime Member'),
    ('associate', 'Associate Member'),
)
	membertype = models.CharField(choices=MEMBER_TYPE, max_length=200)
	memberfees = models.IntegerField(null=True)
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	paymentscreen = models.FileField(upload_to = 'members')

	def get_absolute_url(self):
		print(self.id)
		return reverse('home')


class Eposter(models.Model):
	epostertitle = models.CharField(max_length=255)
	posterfile = models.FileField(upload_to = 'eposter')

	def __str__(self):
		return self.epostertitle

class Homeslider(models.Model):
	home_type = (
    ('',''),
    ('active', 'active'),
	)	
	slidertitle = models.CharField(max_length=225)
	slider = models.FileField(upload_to ='slider')
	sliderlink = models.CharField(max_length=225, null=True, blank=True)
	homeclass = models.CharField(choices=home_type, max_length=200, null=True, blank=True)

	def __str__(self):
		return self.slidertitle
		

class ContactUs(models.Model):

    name= models.CharField(max_length=30)
    email = models.EmailField(max_length=75)
    message = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.name)

