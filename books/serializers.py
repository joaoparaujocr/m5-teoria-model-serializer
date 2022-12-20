from rest_framework import serializers
from .models import Book, Copy


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    copies = CopySerializer(many=True)

    class Meta:
        model = Book
        fields = ["id", "title", "copies"]
