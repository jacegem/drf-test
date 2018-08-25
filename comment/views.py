from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def comment_list(request):
    # 댓글 조회
    if request.method == 'GET':
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    # 댓글 생성
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    # ----- YAML below for Swagger -----
    """
    description: This API deletes/uninstalls a device.
    parameters:
      - name: message
        type: string
        required: true
        location: form
      - name: birthmark
        type: string
        required: true
        location: form
    """
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 특정 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 특정 댓글 수정
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 특정 댓글 삭제
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
