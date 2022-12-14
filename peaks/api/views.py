from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import MountainPeak
from .serializers import MountainPeakSerializer

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class MountainPeaksViewSet(viewsets.ModelViewSet):
    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer


class PeaksDetailAPIView(generics.RetrieveAPIView):
    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer


class PeaksListCreateAPIView(generics.ListCreateAPIView):
    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer


class PeaksUpdateAPIView(generics.UpdateAPIView):
    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class PeaksDestroyAPIView(generics.DestroyAPIView):
    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


@api_view(['POST'])
def get_precise_list(request):
    tleftx = int(request.data["tleft"].split(":")[0])
    trightx = int(request.data["tright"].split(":")[0])
    bleftx = int(request.data["bleft"].split(":")[0])
    brightx = int(request.data["bright"].split(":")[0])
    tlefty = int(request.data["tleft"].split(":")[1])
    trighty = int(request.data["tright"].split(":")[1])
    blefty = int(request.data["bleft"].split(":")[1])
    brighty = int(request.data["bright"].split(":")[1])
    qs = []

    polygon = Polygon([(tleftx, tlefty), (trightx, trighty), (brightx, brighty), (bleftx, blefty)])
    queryset = MountainPeak.objects.all().values()
    for i in queryset:
        if polygon.contains(Point(i['lat'], i['long'])):
            qs.append(i)
    if qs:
        serializer = MountainPeakSerializer(data=qs, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    else:
        return Response({"Invalid": "no data found"})
