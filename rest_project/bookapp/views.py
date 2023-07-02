from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Book,Author
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorController(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
# ModelSerializer
class getAllBooks(APIView):


    class OutputController(serializers.ModelSerializer):
        author=AuthorController()
        class Meta:
            model = Book
            fields = '__all__'
            # fields = ('id', 'author')

    def get(self, request):
        if request.method == 'GET':
            data = Book.objects.all()
            serializer = self.OutputController(data, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'method not allowed', 'status': 404})

# Serializer: The Serializer class is a base class that allows you to define custom serializers with
# fine-grained control over fields and validation. It requires you to explicitly define each field in the
# serializer.
# Example:-

class BookSerializerSimple(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    publication_date = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.save()
        return instance

# The HyperlinkedSerializer is a base class that allows you to create custom serializers with hyperlinks
# for related models. It provides flexibility in defining relationships and specifying hyperlinks explicitly.

class BookSerializerHyperlinked(APIView):
    class OutputSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.IntegerField(read_only=True)
        title = serializers.CharField(max_length=100)
        author = serializers.HyperlinkedRelatedField(
            view_name='author-detail',
            queryset=Author.objects.all(),
            lookup_field='id'
        )
        publication_date = serializers.DateField()

        def create(self, validated_data):
            return Book.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.author = validated_data.get('author', instance.author)
            instance.publication_date = validated_data.get('publication_date', instance.publication_date)
            instance.save()
            return instance


