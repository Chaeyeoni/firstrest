from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id', 'title', 'body']
        read_only_fields = ('body',)
        #윗줄 코드는 body 는 수정불가능 
    
        # fields = '__all__'