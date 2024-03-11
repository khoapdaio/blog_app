import numbers

from django.core.paginator import Paginator
from django.shortcuts import render

from Blog.models import Category, Post


# Create your views here.
def home(request):
	return render(request, 'home.html', {'categories': Category.objects.all()})


def danhSach(request):
	query = request.GET.get('category', None)
	page_number = request.GET.get('page_number')

	if query is not None:
		posts = (
			Post.objects
			.filter(category_id=query)
			.values_list("id", "title", "photo", "meta_description", "publish_date", "author__post", named=True)

		)
	else:
		posts = (
			Post.objects
			.values_list("id", "title", "photo", "meta_description", "publish_date", "author__post", named=True)

		)
	page_post = Paginator(posts, 10)

	if type(page_number) is not numbers:
		posts = page_post.page(1)
	elif page_number > page_post.num_pages:
		posts = page_post.page(page_post.num_pages)
	context = {
		'categories': Category.objects.all(),
		'posts': posts,
		'query': query
	}

	return render(request, "posts/danh-sach.html", context)


def chiTiet(request, id):
	return render(request, "posts/chi-tiet.html", {'post': Post.objects.get(pk=id)})


def lienHe(request):
	return render(request, 'contact.html', {})
