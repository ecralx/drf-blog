from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from blog.authentication.models import CustomUser
from blog.authentication.serializers import (
    UserSerializer,
    AuthSerializer,
)


@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"details": "CSRF cookie set"})


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def create(self, *args, **kwargs):
        return Response({}, status=404)

    def destroy(self, *args, **kwargs):
        return Response({}, status=404)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


@api_view(["POST"])
def login_view(request):
    serializer = AuthSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data["email"]
        password = serializer.data["password"]
        user = authenticate(email=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"detail": "Success"})
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )


@api_view(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({"done": True}, status=200)
