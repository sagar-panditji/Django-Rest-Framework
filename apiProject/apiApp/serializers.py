from rest_framework import serializers
from apiApp import models

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=256)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=256)
    def create(self,validated_data):
        return models.Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance