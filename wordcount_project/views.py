from django.http import HttpResponse
from django.shortcuts import render

# This is a wrong approach
# def home(request):
# 	return HttpResponse("hello")


# Using render to call template and pass a dictionary
# def home(request):
# 	return render(request, 'home.html', {'hithere':'this is me'})

def home(request):
	return render(request, 'home.html')


def count(request):
	return render(request, 'count.html')