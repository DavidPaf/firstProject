from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, BookMiniSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
