from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.views import APIView

class WazeEndpointHandler(APIView):
  renderer_classes = (renderers.UnicodeJSONRenderer, renderers.JSONRenderer)

  def get(self, request, *args, **kwargs):
    response = {}

    if 'x' in request.GET and 'y' in request.GET and 'z' in request.GET:
      x = request.GET['x'][0]
      y = request.GET['y'][0]
      z = request.GET['z'][0]

    response = (x, y, z) # TODO
    return Response(response)
