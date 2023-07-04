from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    types= serializers.CharField()
    summary = serializers.CharField()
    body = serializers.CharField()
    photo = serializers.ImageField()