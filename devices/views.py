from rest_framework import generics, renderers
from rest_framework.response import Response
from models import Device, Status, Command
from serializers import DeviceSerializer, StatusSerializer, CommandSerializer

#Devices
##################################################

class DeviceListView(generics.ListCreateAPIView):
    #comment this in to disable Django Rest Framework Browsable API
    #renderer_classes = [renderers.JSONRenderer]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetailsView(generics.RetrieveAPIView):
    #comment this in to disable Django Rest Framework Browsable API
    #renderer_classes = [renderers.JSONRenderer]
    serializer_class = DeviceSerializer

    def get_object(self):
        uuid = self.kwargs['uuid']
        return Device.objects.get(uuid=uuid)

class DeviceStatusesView(generics.ListAPIView):
    #comment this in to disable Django Rest Framework Browsable API
    #renderer_classes = [renderers.JSONRenderer]
    serializer_class = StatusSerializer

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        return Status.objects.filter(device_id = uuid)

#Statuses
##################################################

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class StatusListView(generics.ListCreateAPIView):
    #comment this in to disable Django Rest Framework Browsable API
    #renderer_classes = [renderers.JSONRenderer]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        status = Status()
        status.cpu_load = request.data['cpu_load']
        status.used_memory = request.data['used_memory']
        status.total_memory = request.data['total_memory']
        status.used_disk = request.data['used_disk']
        status.total_disk = request.data['total_disk']

        device = Device.objects.get(uuid=request.data['device'])
        status.device = device

        status.ip = get_client_ip(request)
        status.save()
        serializer = StatusSerializer()

        return Response(serializer.to_representation(status))



#Commands
##################################################

class CommandListView(generics.ListCreateAPIView):
    #comment this in to disable Django Rest Framework Browsable API
    #renderer_classes = [renderers.JSONRenderer]
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    def get_queryset(self):
        device = self.kwargs['device']
        return Command.objects.filter(device=device, status=0)