from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.views import APIView

class WazeEndpointHandler(APIView):
  renderer_classes = (renderers.UnicodeJSONRenderer, renderers.JSONRenderer)

  def get(self, request, *args, **kwargs):
    response = []

    if 'time_from' in request.GET and 'time_to' in request.GET:
      # TODO - validate
      time_from = request.GET['time_from']
      time_to = request.GET['time_to']
    else:
      time_from = '2014-03-23 00'
      time_to = '2014-03-25 00'

    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB = 'waze'
    MONGO_COLLECTION = 'jams'

    conn = pymongo.Connection(MONGO_HOST, MONGO_PORT)
    collection = conn[MONGO_DB][MONGO_COLLECTION]
    # TODO - arrumar o formato do retorno
    for doc in collection.find({'endtime': {'$gt': time_from, '$lt': time_to}}):
      response.append(doc)

    return Response(response)
