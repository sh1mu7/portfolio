from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from ..models import Post, Category, Comment


# Post
class PostListAPI(GenericAPIView, ListModelMixin):
    permission_classes = [AllowAny]
    queryset = Post.PostObjects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostCreateAPI(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Post.PostObjects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUpdateAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Post.PostObjects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostRetrieveAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [AllowAny]
    queryset = Post.PostObjects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostDeleteAPI(GenericAPIView, DestroyModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Post.PostObjects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Comment
class CommentListAPI(GenericAPIView, ListModelMixin):
    permission_classes = [IsAdminUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommentCreateAPI(GenericAPIView, CreateModelMixin):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentUpdateAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CommentRetrieveAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CommentDeleteAPI(GenericAPIView, DestroyModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Category
class CategoryListAPI(GenericAPIView, ListModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryCreateAPI(GenericAPIView, CreateModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryUpdateAPI(GenericAPIView, UpdateModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CategoryRetrieveAPI(GenericAPIView, RetrieveModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryDeleteAPI(GenericAPIView, DestroyModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
