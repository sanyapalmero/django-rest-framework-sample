from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Book
        fields = ("id", "name", "price", "pages", "published_at", "author")

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.published_at = validated_data.get(
            "published_at", instance.published_at
        )
        instance.pages = validated_data.get("pages", instance.pages)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "books"]
