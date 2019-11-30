from collections import OrderedDict

from django.shortcuts import render_to_response

from main.models import *


def index(request):
    return render_to_response('main/index.html')


def schedule(request):
    all_doctors = OrderedDict()
    for each in Doctor.TYPE:
        all_doctors[each[1]] = Doctor.objects.filter(type=each[0])

    context = {
        'all_doctors': all_doctors,
    }
    return render_to_response('main/schedule.html', context=context)


def contacts(request):
    context = {
        'contacts': Contact.objects.get(id=1)
    }
    return render_to_response('main/contacts.html', context=context)


def photo(request):
    context = {
        'photos': Photo.objects.all()
    }
    return render_to_response('main/photo.html', context=context)


def price(request):
    context = {
        'price_lists': PriceList.objects.all().prefetch_related('price_set'),
    }
    return render_to_response('main/price.html', context=context)


def doctors(request):
    context = {
        'doctors': Doctor.objects.all(),
    }
    return render_to_response('main/doctors.html', context=context)


def documents(request):
    context = {
        'documents': Document.objects.all()
    }
    return render_to_response('main/documents.html', context=context)


def document(request, pk):
    context = {
        'document': Document.objects.prefetch_related('documentimage_set').get(pk=pk),
    }
    return render_to_response('main/document.html', context=context)


def announcements(request):
    context = {
        'announcements': Announcement.objects.all()
    }
    return render_to_response('main/announcements.html', context=context)
