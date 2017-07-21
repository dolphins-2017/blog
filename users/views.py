from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, UserChangeForm

class index(View):
	def get(self, request):
		return render(request, 'users/index.html')

class Login(View):
	form = AuthenticationForm
	def get(self, request):
		context = {
			'name': request.GET.get('name', None),
			'loginForm': self.form(initial={'username':request.GET.get('name', None)})
		}

		return render(request, 'users/login.html', context)

	def post(self, request):
		form = self.form( request, request.POST )

		if form.is_valid():
			print(type(form.get_user()))
			login(request, form.get_user() )
			
			return redirect( '/blog' )
		else:
			context = {
				'loginForm': form
			}

			return render( request, 'users/login.html', context )

class Logout(View):
	def get(self, request):
		logout(request)

		return redirect('/')


class singup(View):
	form = UserCreationForm

	def get(self, request):
		context = {
			'creationForm': self.form()
		}

		return render(request, 'users/singup.html', context)

	def post(self, request):
		
		form = self.form(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/users/login?name={}'.format(request.POST.get('username')))
		else:
			context = {
				'creationForm': form
			}
			return render(request, 'users/singup.html', context)
