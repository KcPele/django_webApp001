from django.shortcuts import render


posts = [
   {
   		'author':'Kcpele',
   		'title':'Blog post 1',
   		'content':'First post content',
   		'date_posted':'August 78'
   },
   {
   		'author':'Gift',
   		'title':'Blog post 2',
   		'content':'second post content',
   		'date_posted':'August 78'
   }
]

def home(request):
	context = {
	'posts':posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})