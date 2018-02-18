from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import RegisterForm

def index(request):
	context = {
		'user': request.user,
	}
	return render(request, 'index.html', context)

@login_required
def mypage(request):
	context = {
		'user': request.user,
	}
	return render(request, 'mypage.html', context)

def regist(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form': form,
	}
	return render(request, 'regist.html', context)

@require_POST
def regist_save(request):
	form = RegisterForm(request.POST)
	if form.is_valid():
		user = form.save()
		return redirect('mypage')

	context = {
		'form': form,
	}

	return render(request, 'regist.html', context)