from rest_framework import viewsets 

from .models import Post
from .serializer import PostSerializer

#CBV
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.
