from rest_framework import serializers
from apps.main.models import Category, FAQ
from slugify import slugify

# 1. Listeleyen Serializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "is_active", "created_at", "updated_at"]


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name","is_active"]

    def create(self, validated_data):
        print(validated_data)
        slug = slugify(validated_data.get("name"))

        # name=value
        return Category.objects.create(**validated_data, slug=slug)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer"]


class FAQCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["question", "answer"]

    def create(self, validated_data):
        return FAQ.objects.create(**validated_data)


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "is_active", "slug", "created_at", "updated_at"]

    def update(self, instance, validated_data):
        if name := validated_data.get("name"):
            instance.slug = slugify(name)
            instance.name = name
            

            print(f"guncellendi -> isim: {instance.name} | slug: {instance.slug}")
            
        if "is_active" in validated_data:
            instance.is_active = validated_data.get("is_active")

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
 