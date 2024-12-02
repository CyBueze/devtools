from rest_framework import serializers
from .models import DevTool

class DevToolSerializer(serializers.ModelSerializer):
    """
    Serializer to convert DevTool model into JSON objects and vice versa
    """
    class Meta:
        model = DevTool
        fields = "__all__"
