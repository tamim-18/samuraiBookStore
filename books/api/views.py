from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from books.api.serializers import BookSerializer
from books.models import Book


class BooksAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):

        # sort and search (exact search)
        title = request.query_params.get('title')
        author = request.query_params.get('author')
        genre = request.query_params.get('genre')
        if title:
            self.queryset = self.queryset.filter(title=title)
        if author:
            self.queryset = self.queryset.filter(author=author)
        if genre:
            self.queryset = self.queryset.filter(genre=genre)

        # sort
        sort = request.query_params.get('sort')
        if sort:
            self.queryset = self.queryset.order_by(sort)

        return Response(
            data={
                'books': self.serializer_class(self.queryset.all(), many=True).data,
            },
        )


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        try:
            if Book.objects.get(pk=kwargs['pk']):
                return self.retrieve(request, *args, **kwargs)
        except Book.DoesNotExist:
            return Response(
                data={'message': f"book with id: {kwargs['pk']} was not found"},
                status=404,
            )

    def put(self, request, *args, **kwargs):
        try:
            if Book.objects.get(pk=kwargs['pk']):
                return self.update(request, *args, **kwargs)
        except Book.DoesNotExist:
            return Response(
                data={'message': f"book with id: {kwargs['pk']} was not found"},
                status=404,
            )
