import django_filters
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView
from django.core.exceptions import ObjectDoesNotExist

from .filters import PerevalFilter
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer


class PerevalList(ListAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer
    filterset_class = PerevalFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]



@api_view(['POST'])
def submit_data(request):
    serializer = Pereval_addedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_data(request, pk):
    try:
        pereval = Pereval_added.objects.get(pk=pk)
    except Exception:
        return Response(status=404)

    serializer = Pereval_addedSerializer(pereval)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_data(request, pk):
    try:
        pereval = Pereval_added.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'state': 0, 'message': 'Pereval does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if pereval.status != 'new':
        return Response({'state': 0, 'message': 'Pereval status is not "new'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = PerevalUpdateSerializer(pereval, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'state': 1}, status.HTTP_200_OK)
    return Response({'state': 0, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
