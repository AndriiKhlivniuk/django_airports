from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Airport
from .serializers import AirportSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

@api_view(['GET'])
def airport_list(request):
    airports = Airport.objects.all()
    serializer = AirportSerializer(airports, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def airport_ident(request, ident):
    try:
        airport = Airport.objects.get(ident=ident)
    except Airport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AirportSerializer(airport)
    return Response(serializer.data)