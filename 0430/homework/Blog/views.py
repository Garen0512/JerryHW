from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .models import *

def homepage(request):
	if request.method == 'POST':
		pk = request.POST.get('pk')
		Post.objects.get(pk=pk).delete()
	post_list = Post.objects.all()
	return render(request, 'homepage.html', {'post_list': post_list})

def homepage_1(request):
	if request.method == 'POST':
		text = request.POST.get('text')
		comment = request.POST.get('comment')
		Post.objects.create(text=text, comment=comment)
		return redirect('/blog')
	return render(request, 'homepage_1.html')

def homepage_2(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.text = request.POST.get('text')
		post.comment = request.POST.get('comment')
		post.save()
		return redirect('/blog')
	return render(request, 'homepage_2.html', {'post': post})