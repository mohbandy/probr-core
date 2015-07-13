from views import CommandTemplateListView, CommandTemplateDetailsView, DeviceListView, DeviceDetailsView,CommandListView, CommandDetailsView, StatusList
from django.conf.urls import url


urlpatterns = [
    #Devices

    #list of all devices
    url(r'^api/devices/$', DeviceListView.as_view(), name='device-list'),

    #details of a device by uuid
    url(r'^api/devices/(?P<uuid>[^/]+)/+$', DeviceDetailsView.as_view(), name='device-details'),
    ###########################################

    #Statuses

    #list of all statuses
    url(r'^api/statuses/$', StatusList.as_view(), name='status-list'),

    ###########################################

    #Commands

    #list of all commands
    url(r'^api/commands/$', CommandListView.as_view(), name='command-list'),

    #details of a command by uuid
    url(r'^api/commands/(?P<uuid>[^/]+)/+$', CommandDetailsView.as_view(), name='command-details'),

    #list of all commandtemplates
    url(r'^api/commandtemplates/$', CommandTemplateListView.as_view(), name='commandtemplate-list'),

    #details of a commandtempate by uuid
    url(r'^api/commandtemplates/(?P<pk>[^/]+)/+$', CommandTemplateDetailsView.as_view(), name='commandtemplate-details'),

]