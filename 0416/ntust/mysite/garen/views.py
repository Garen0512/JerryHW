from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import myself

#Create your views here.
def index(request):
    me = myself.objects.all()
    return render_to_response('garen/menu.html',locals())