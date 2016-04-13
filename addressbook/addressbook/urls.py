from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
#from forms_builder.forms import forms, urls
import contacts.views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list',),
    url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(), name='contacts-view',),
    url(r'^new$', contacts.views.CreateContactView.as_view(), name='contacts-new',),
    url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contacts-edit',),
    url(r'^edit/(?P<pk>\d+)/addresses$', contacts.views.EditContactAddressView.as_view(),name='contacts-edit-addresses',),
    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(), name='contacts-delete',),
#Should be removed later
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^forms/', include(forms_builder.forms.urls)),
)
urlpatterns += staticfiles_urlpatterns()