import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    csv_file_path = settings.BUS_STATION_CSV
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations_list = list(reader)
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    print(reader)
    return render(request, 'stations/index.html', context)
