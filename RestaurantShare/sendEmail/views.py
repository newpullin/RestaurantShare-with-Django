from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def sendEmail(request):
    return HttpResponseRedirect(reverse('index'))
    return HttpResponse("sendEmail")