from django.http import HttpResponse
from django.shortcuts import render
import operator

# This is a wrong approach
# def home(request):
# 	return HttpResponse("hello")


# Using render to call template and pass a dictionary
# def home(request):
# 	return render(request, 'home.html', {'hithere':'this is me'})

def home(request):
	return render(request, 'home.html')


def count(request):
	# pull parameters from the previous page with its name
	fulltext = request.GET['fulltext']
	word_count = len(fulltext.split())

	word_list = fulltext.split()
	worddict = {}

	for word in word_list:
		if word in worddict:
			# increment count of word
			worddict[word] += 1
		else:
			# add the new word
			worddict[word] = 1

	sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse = True) 

	return render(request, 'count.html', {'fulltext':fulltext, 'count':word_count, 'sortedwords':sortedwords
		})	
