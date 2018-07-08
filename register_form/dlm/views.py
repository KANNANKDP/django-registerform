from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.

from register import models

def homePageView(request):
	return render(request,'home.html',{})

def dashPageView(request):
	if(request.session.has_key('log_in')==True):
		if(request.session['log_in']==True):
			# return HttpResponse('session is active now...')
			data = models.UserDetail.objects.all()
			user_data = {
				'users' : data
				,'name' : request.session['name']
			}
			return render(request,'dashboard.html',user_data)
	elif(request.session.has_key('log_in')==False):
		return redirect('/login/')

	else:
		return redirect('/login/')

def logout(request):
	if(request.session.has_key('log_in')==True):
		del request.session['log_in']
		del request.session['name']
		request.session.flush()
		request.session.modified = True
		return redirect('/login/')