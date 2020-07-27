from django.contrib import admin

# Register your models here.
from .models import Officebearers, Pastofficebearers, Pastmembers, Doanews, Doaevents, Archivejournal, Awards, members,Newmember, Eposter, Homeslider

admin.site.register(Officebearers)
admin.site.register(Pastofficebearers)
admin.site.register(Pastmembers)
admin.site.register(Doanews)
admin.site.register(Doaevents)
admin.site.register(Archivejournal)
admin.site.register(Awards)
admin.site.register(members)
admin.site.register(Eposter)
admin.site.register(Homeslider)