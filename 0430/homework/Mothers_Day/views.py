from django.shortcuts import render
from .models import *

# Create your views here.

def mother(request):
	comment = ''
	if request.method == 'POST':
		comment = request.POST.get('comment')
		Mother.objects.create(content=comment)
	return render(request, 'motherday.html', {'comment': comment})
