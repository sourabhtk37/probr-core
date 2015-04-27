from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser, FormParser
from models import Capture
from serializers import CaptureSerializer

# Create your views here.


@api_view(['POST','GET'])
@renderer_classes((JSONRenderer,))
@parser_classes((MultiPartParser, FormParser,))
def upload_form(request):
    if request.method == 'POST':
        instance = Capture(pcap=request.FILES['pcap'],longitude=request.DATA['longitude'],latitude=request.DATA['latitude'])
        print("Tags: " + request.DATA['tags'])
        instance.tags.add(request.DATA['tags'])
        instance.save()
        return Response('Capture upload successful')

    elif request.method == 'GET':
        captures = Capture.objects.all();
        serializer = CaptureSerializer(captures,many=True);
        return Response(serializer.data)

