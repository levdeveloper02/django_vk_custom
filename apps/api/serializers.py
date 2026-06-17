from rest_framework import serializers
from apps.main.models import Category, FAQ
from slugify import slugify

# 1. Listeleyen Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "created_at", "updated_at"]

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

    def create(self, validated_data):
        print(validated_data)
        slug=slugify(validated_data.get("name"))

        return Category.objects.create(**validated_data, slug=slug) #name=value


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer"]


class FAQCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=FAQ
        fields=["question", "answer"]

    def create(self, validated_data):
        return FAQ.objects.create(**validated_data)




            


