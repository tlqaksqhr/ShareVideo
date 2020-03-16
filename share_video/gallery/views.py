from django.shortcuts import render
from django.http import HttpResponse

# SPA Using react
def index(request):
    return HttpResponse("Index page")

def video_list(request):
    return HttpResponse("Video List")

def get_video(request):
    return HttpResponse("Get Specific Video")

def video_upload(request):
    return HttpResponse("Video Upload")

def video_modify(request):
    return HttpResponse("Video Modify")

def add_comment(request):
    return HttpResponse("Add Comment")

def remove_comment(request):
    return HttpResponse("Remove Comment")

def modifiy_comment(request):
    return HttpResponse("Modify Comment")

def get_comments(request):
    return HttpResponse("Get All Comment")

def get_all_favorite(request):
    return HttpResponse("Get All Favorite")

def favorite_count(request):
    return HttpResponse("Favorite Count")

def add_favorite(request):
    return HttpResponse("Add Favorite to video")

def remove_favorite(request):
    return HttpResponse("Remove Favorite to video")