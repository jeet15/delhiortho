from django.urls import path
from . import views
from .views import HomeView, PastOfficebearersView, OfficebearersView, EventView , EventDetailView ,PastpresidentView, DoanewsView, DoaAllEventView, DoaawardsView, EventDetailView,EposterView, covid, doa_member, member_area, member_list, member_profile, edit_member_profile, edit_member_image, edit_member_certificate, edit_member_degree

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('doaevent/<int:pk>', EventDetailView.as_view(), name="event_details"),
	# path('', views.home, name="home"),
	path('list.html', EventView.as_view(), name="eventlist"),
	path('event/<int:pk>', EventDetailView.as_view(), name="event-detail"),
	path('member-registration.html', views.doa_member, name="member-registration"),	
	path('president-message.html', views.president_message, name="presidentmessage"),
	path('secretary-message.html', views.secretary_message, name="secretarymessage"),
	path('office-bearers-2018-19.html', PastOfficebearersView.as_view(), name="officebearers2018_19"),
	path('office-bearers-2019-20.html', OfficebearersView.as_view(), name="officebearers2019_20"),
	path('doa-elections-2019-2020.html', views.doaelections2019_2020, name="doaelections2019_2020"),
	path('past-presidents-and-secretaries.html', PastpresidentView.as_view(), name="past_presidents_and_secretaries"),
	path('doa-news.html', DoanewsView.as_view(), name="doa_news"),
	path('doa-events.html', DoaAllEventView.as_view(), name="doa_events"),
	path('eposter.html', EposterView.as_view(), name="eposter"),
	path('archived-events.html', views.archived_events, name="archived_events"),
	path('doa-fellowship.html', views.doa_fellowship, name="doa_fellowship"),
	path('doacon-award-2019.html', DoaawardsView.as_view(), name="doacon_award2019"),
	path('doa-journal.html', views.doa_journal, name="doa_journal"),
	path('archive.html', views.archive, name="archive"),
	path('doa-journal-archive.html', views.doa_journal_archive, name="doa_journal_archive"),
	path('subspeciality.html', views.subspeciality, name="subspeciality"),
	path('photo-gallery.html', views.photo_gallery, name="photo_gallery"),
	path('contact.html', views.contact, name="contact"),
	path('member-area.html', views.member_area, name="member-area"),
	path('member-login.html', views.member_login, name="member-login"),
	path('covid_19.html', views.covid, name="covid_19"),
	path('member-list.html', views.member_list, name="member-list"),
	path('member-profile.html/<username>', views.member_profile, name="member-profile"),
	path('edit-member-profile.html/<username>', views.edit_member_profile, name="edit-member-profile"),
	path('member-image/<username>', views.edit_member_image, name="member-image"),
	path('member-degree/<username>', views.edit_member_degree, name="member-degree"),
	path('member-certificate/<username>', views.edit_member_certificate, name="member-certificate"),
	
]