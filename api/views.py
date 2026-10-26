
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from drf_spectacular.utils import extend_schema

from .models import Book, Category
from .serializers import (
    BookSerializer,
    CategorySerializer,
    CategoryDetailSerializer,
)


@extend_schema(
    summary="Список книг и создание новой книги",
    description="Получение списка всех книг или добавление новой книги."
)
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(
    summary="Просмотр, изменение и удаление книги",
    description="Получение, обновление или удаление книги по её ID."
)
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(
    summary="Детальная категория с книгами",
    description="Получение категории с вложенными данными (книги в категории).",
    responses={200: CategoryDetailSerializer}
)
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.prefetch_related('books')
    serializer_class = CategoryDetailSerializer
