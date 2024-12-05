from django.urls import path ,include
from . import views

urlpatterns = [
    path('books/',views.book_list,name='book-list'),
    path('books/<int:pk>',views.book_detail,name='book-detail')
]
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)