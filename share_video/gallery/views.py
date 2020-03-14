from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")

def video_list(request):
    return HttpResponse("Video List")

def video_upload(request):
    return HttpResponse("Video Upload")