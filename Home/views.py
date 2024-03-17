from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from Blog.models import Category, Post


# Create your views here.
def home(request):
	context = {
		'categories': Category.objects.filter(active=True).all(),
		'posts': Post.objects.filter(published=True)
		.values_list("publish_date", named=True)
	}

	return render(request, 'home.html', context)


def danhSach(request):
	posts = (
		Post.objects.filter(published=True)
		.values_list("id", "title", "photo", "meta_description", "publish_date", "author", named=True)
	)
	page_post = Paginator(posts, 5)
	posts = page_post.page(1)
	context = {
		'categories': Category.objects.filter(active=True).all(),
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
		lookups = lookups & Q(category_id=category_search)
	if title_search != '' and title_search is not None:
		lookups = lookups & Q(title__contains=title_search)
	if date_search != '' and date_search is not None:
		lookups = lookups & Q(date_created__gte=date_search)

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
		'categories': Category.objects.filter(active=True).all(),
		'posts': posts,
		'title_search': title_search,
		'date_search': date_search,
		'query': int(category_search) if (category_search is not None and category_search != '') else None
	}

	return render(request, "posts/danh-sach.html", context)


def chiTiet(request, id):
	context = {
		'categories': Category.objects.filter(active=True).all(),
		'post': Post.objects.get(pk=id)
	}

	return render(request, "posts/chi-tiet.html", context)


def lienHe(request):
	context = {
		'categories': Category.objects.filter(active=True).all(),
		'lienHe': Post.objects.get(pk=32)
	}

	return render(request, 'contact.html', context)


def gioiThieu(request):
	context = {
		'categories': Category.objects.filter(active=True).all(),
		'gioiThieu': Post.objects.get(pk=33)
	}

	return render(request, 'about.html', context)
