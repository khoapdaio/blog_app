from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from Blog.models import Category, Post


# Create your views here.
def home(request):
	return render(request, 'home.html', {'categories': Category.objects.all()})


def danhSach(request):
	posts = (
		Post.objects.filter(published=True)
		.values_list("id", "title", "photo", "meta_description", "publish_date", "author", named=True)
	)
	page_post = Paginator(posts, 5)
	posts = page_post.page(1)
	context = {
		'categories': Category.objects.all(),
		'posts': posts,
	}

	return render(request, "posts/danh-sach.html", context)


def search(request):
	category_search = request.GET.get('category', None)
	title_search = request.GET.get('title', None)
	date_search = request.GET.get('date', None)
	page_number = int(request.GET.get('page', 1))

	lookups = Q(published=True)

	if category_search != '' and category_search is not None:
		lookups = lookups | Q(category_id=category_search)
	if title_search != '' and title_search is not None:
		lookups = lookups | Q(title__contains=title_search)
	if date_search != '' and date_search is not None:
		lookups = lookups | Q(date_created__gte=date_search)

	posts = (
		Post.objects
		.filter(
			lookups
		)
		.values_list(
			"id",
			"title",
			"photo",
			"meta_description",
			"publish_date",
			"author",
			named=True)
	)

	page_post = Paginator(posts, 10)

	if type(page_number) is not int:
		posts = page_post.page(1)
	elif page_number > page_post.num_pages:
		posts = page_post.page(page_post.num_pages)
	else:
		posts = page_post.page(page_number)

	context = {
		'categories': Category.objects.all(),
		'posts': posts,
		'query': category_search
	}

	return render(request, "posts/danh-sach.html", context)


def chiTiet(request, id):
	return render(request, "posts/chi-tiet.html", {'post': Post.objects.get(pk=id)})


def lienHe(request):
	context = {
		'lienHe': Post.objects.get(pk=32)
	}

	return render(request, 'contact.html', context)


def gioiThieu(request):
	context = {
		'gioiThieu': Post.objects.get(pk=33)
	}

	return render(request, 'about.html', context)
