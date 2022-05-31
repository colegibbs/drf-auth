from rest_framework import serializers
from .models import book

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'description', 'publication_date', 'created_at', 'updated_at')
    model = book