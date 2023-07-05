from rest_framework import serializers
from .models import Book, Author



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date']


class BookSerializer(serializers.ModelSerializer):
    author=AuthorSerializer(required=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']

    # If you want to do partially update any fields including the foreign key elements
    # here by using for loop you can update the fields of foreign key elements but Primary key is required
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author_instance = instance.author
            for attr, value in author_data.items():
                setattr(author_instance, attr, value)
            # author_serializer = AuthorSerializer(instance.author, data=author_data,partial=True)
            # if author_serializer.is_valid():
            author_instance.save()
            # else:
            #     raise serializers.ValidationError(author_serializer.errors)
        return super().update(instance, validated_data)

    def validate_title(self, value):
        # Example of field-specific validation
        if len (value) < 5:
            raise serializers.ValidationError ("Title must be at least 5 characters long.")
        return value

    # def validate(self, attrs):
    #     # Example of cross-field validation
    #     if attrs['publication_date'].year > 2023:
    #         raise serializers.ValidationError("Invalid publication date.")
    #     return attrs

    def create(self, validated_data):
        # Example of custom create method
        book = Book.objects.create (**validated_data)
        return book

    # def update(self, instance, validated_data):
    #     # Example of custom update method
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.publication_date = validated_data.get('publication_date', instance.publication_date)
    #     instance.save()
    #     return instance
