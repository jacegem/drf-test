from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # HTTP GET /blog/post/
    # HTTP GET /blog/post/?search=
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            qs = qs.filter(message__icontains=search)
        return qs

    # HTTP GET /blog/post/get_django/
    @list_route()
    def get_django(self, req):
        qs = self.get_queryset().filter(message__icontains='m')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # HTTP PATCH /blog/post/{pk}/set_modified
    @detail_route(methods=['get', 'patch'])
    def set_modified(self, req, pk):
        instance = self.get_object()
        instance.message = instance.message + '(modified)'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
