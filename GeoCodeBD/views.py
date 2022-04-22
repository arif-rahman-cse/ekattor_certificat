from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from GeoCodeBD.models import District, Upazila, Union
from GeoCodeBD.serializer import DistrictsSerializer, UpazilaSerializer, UnionSerializer


@login_required
def get_district_by_division(request):
    if request.method == "GET":
        division_id = request.GET.get('division_id', None)
        districts = District.objects.filter(division=division_id)
        serializer = DistrictsSerializer(districts, many=True)
        return JsonResponse(serializer.data, safe=False)


@login_required
def get_thana_by_district(request):
    if request.method == "GET":
        district_id = request.GET.get('district_id', None)
        upazila = Upazila.objects.filter(district=district_id)
        serializer = UpazilaSerializer(upazila, many=True)
        return JsonResponse(serializer.data, safe=False)


@login_required
def get_union_by_thana(request):
    if request.method == "GET":
        thana_id = request.GET.get('thana_id', None)
        print(thana_id)
        unions = Union.objects.filter(upazila=thana_id)
        serializer = UnionSerializer(unions, many=True)
        return JsonResponse(serializer.data, safe=False)
