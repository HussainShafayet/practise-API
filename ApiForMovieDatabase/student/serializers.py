from rest_framework import serializers
from .models import Student

""" class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__' """
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    reg_no = serializers.IntegerField()
    dept = serializers.CharField(max_length=100)
    session = serializers.CharField(max_length=100)
    institute = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.reg_no = validated_data.get('reg_no', instance.reg_no)
        instance.dept = validated_data.get('dept', instance.dept)
        instance.session = validated_data.get('session', instance.session)
        instance.institute = validated_data.get('institute', instance.institute)
        instance.save()
        return instance