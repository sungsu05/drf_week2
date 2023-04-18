from rest_framework import serializers
from .models import Articles

class SerializerArticle(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"