from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_user_details(request):
    data = {
        "slackUsername": "netrobe",
        "backend": True,
        "age": 20,
        "bio": "I am a student of UoL that loves coding."
    }
    return Response(data)
