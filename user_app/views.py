from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .authentication import JWTAuthentication


# Create your views here.
class Register(APIView):
    def post(self, request):
        data = request.data

        password_confirm = data.get("password_confirm", None)

        if password_confirm is None:
            raise exceptions.APIException("You must enter password_confirm.")

        if data["password"] != password_confirm:
            raise exceptions.APIException("Unmatched passwords.")

        if User.objects.filter(email=data["email"]).exists():
            raise exceptions.APIException("Email already exists.")

        serializer = UserSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Email")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid Password")

        # Once here, user exists, creating token
        token = JWTAuthentication.generate_jwt(user.id)

        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"message": "logged in", "jwt": token}

        return response

