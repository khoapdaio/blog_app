from django.urls import path

from Home import views

urlpatterns = [
	path('', views.home, name='home'),
	path('danh-sach', views.danhSach, name='danh-sach'),
	path('chi-tiet/<str:id>', views.chiTiet, name='chi-tiet'),
	path('lien-he', views.lienHe, name='lien-he')

]
