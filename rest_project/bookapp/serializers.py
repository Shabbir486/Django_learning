from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        # Example of field-specific validation
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    # def validate(self, attrs):
    #     # Example of cross-field validation
    #     if attrs['publication_date'].year > 2023:
    #         raise serializers.ValidationError("Invalid publication date.")
    #     return attrs

    def create(self, validated_data):
        # Example of custom create method
        book = Book.objects.create(**validated_data)
        return book

    # def update(self, instance, validated_data):
    #     # Example of custom update method
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.publication_date = validated_data.get('publication_date', instance.publication_date)
    #     instance.save()
    #     return instance
