from rest_framework import serializers as s
from .models import *


# class BookSerializer(s.Serializer):
#     bid = s.IntegerField(primary_key=True)
#     title = s.CharField(max_length=50)
#     author = s.CharField(max_length=50)
#     category = s.CharField(max_length=50)
#     pages = s.IntegerField()
#     price = s.IntegerField()
#     published_date = s.DateField()
#     description = s.TextField()

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.bid = validated_data.get('bid', instance.bid)
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.category = validated_data.get('category', instance.category)
#         instance.pages = validated_data.get('pages', instance.pages)
#         instance.price = validated_data.get('price', instance.price)
#         instance.published_date = validated_data.get(
#             'published_date', instance.published_date)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.save()
#         return instance


# class BookSerializer(s.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['bid', 'title', 'author', 'category',
#                   'pages', 'price', 'published_date', 'description']

class UserSerializer(s.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userName', 'pwd']
