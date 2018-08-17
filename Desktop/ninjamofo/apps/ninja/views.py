from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from time import strftime, gmtime
from random import *

def index(request):
	if "count" not in request.session:
		request.session["count"] = []

	if "gold" not in request.session:
		request.session["gold"] = 0
	context = {
		"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
	}
	return render(request, 'ninja/index.html', context)

def farm(request):
	print ("*"*50)
	x = randint(5,10)
	request.session["gold"] += x
	request.session["count"] += [{"gold": x, "name": "farm"}]
	return redirect('/')

def cave (request):
	x = randint(5,10)
	request.session["gold"] += x
	request.session["count"] += [{"gold": x, "name": "cave"}]
	return redirect('/')

def house(request):
	x = randint(2,5)
	request.session["gold"] += x
	request.session["count"] += [{"gold": x, "name": "house"}]
	return redirect('/')

def casino(request):
	x = randint(-50,50)
	request.session["gold"] += x
	request.session["count"] += [{"gold": x, "name": "casino"}]
	return redirect('/')
