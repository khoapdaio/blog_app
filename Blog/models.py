# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.conf import settings
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'category'


class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'tag'


class Author(models.Model):
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.PROTECT,
	)
	website = models.URLField(blank=True)
	bio = models.CharField(max_length=240, blank=True)

	def __str__(self):
		return self.user.get_username()

	class Meta:
		db_table = 'author'


class Post(models.Model):
	class Meta:
		ordering = ["-publish_date"]
		db_table = "posts"

	title = models.CharField(max_length=255, unique=True)
	photo = models.ImageField(upload_to='static/images/')
	subtitle = models.CharField(max_length=255, blank=True)
	slug = models.SlugField(max_length=255, unique=True)
	body = RichTextUploadingField()
	meta_description = models.CharField(max_length=150, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	publish_date = models.DateTimeField(blank=True, null=True)
	published = models.BooleanField(default=False)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	author = models.ForeignKey(Author, on_delete=models.PROTECT)
	tags = models.ManyToManyField(Tag, blank=True)


class Comment(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey("Post", on_delete=models.CASCADE)

	class Meta:
		db_table = "comments"


