from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm

class Index(View):
	def get(self, request):
		context ={
			'posts': Post.objects.all()
		}

		return render(request, 'blog/index.html', context)

class Create(View):
	form = PostForm
	def get(self, request):

		if request.user.is_authenticated:

			context = {
				'postForm': self.form(initial={'user':request.user})
			}

			return render(request, 'blog/create.html', context)
		else:
			return redirect('/users/login')

	def post(self, request):
		form = self.form(request.POST)
		if request.user.is_authenticated:
			if form.is_valid():
				form.save()
				return redirect('/blog')
			else:
				context = {
					'postForm': form
				}

				return render(request, 'blog/create.html', context)
		else:
			return redirect('/users/login')

class Edit(View):
	def get(self, request):
		pass

	def post(self, request):
		pass

class Delete(View):
	def get(self, request):
		pass

	def post(self, request):
		pass
