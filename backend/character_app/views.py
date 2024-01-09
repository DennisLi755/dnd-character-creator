from .models import Character
from .serializers import CharacterSerializer
# Import both APIView and Response from DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
# Create your views here.

class All_characters(APIView):
    # Just like we said before we only want this information available for GET requests therefore we have to place this logic under a GET method. DRF will recognize the `get` method and trigger that method every time a GET request is sent
    def get(self, request):
        character = CharacterSerializer(Character.objects.order_by('name'), many=True)
        # Under response we don't necessarily need to send information in JSON format instead DRF will format our response and make it acceptable for Front-End frameworks
        return Response(character.data)
    
    def post(self, request):
        new_character = CharacterSerializer(data=request.data)
        if new_character.is_valid():
            new_character.save()
            return Response(new_character.data, status=HTTP_201_CREATED)  
        else:
            return Response(new_character.errors, status=HTTP_400_BAD_REQUEST)    
    
class A_character(APIView):
    def get(self, request, id):
        character = None
        if type(id) == int:
            character = Character.objects.get(id=id)
        else:
            character = Character.objects.get(name=id.title())
        return Response(CharacterSerializer(character).data)