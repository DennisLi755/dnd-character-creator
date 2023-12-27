from .models import Character
from .serializers import CharacterSerializer
# Import both APIView and Response from DRF
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class All_characters(APIView):
    # Just like we said before we only want this information available for GET requests therefore we have to place this logic under a GET method. DRF will recognize the `get` method and trigger that method every time a GET request is sent
    def get(self, request):
        character = CharacterSerializer(Character.objects.order_by('name'), many=True)
        # Under response we don't necessarily need to send information in JSON format instead DRF will format our response and make it acceptable for Front-End frameworks
        return Response(character.data)