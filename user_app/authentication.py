import jwt, datetime
from calorina import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return None

        try:
            payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Not Authenticated")
        user = User.objects.get(id=payload["user_id"])

        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        return (user, None)

    @staticmethod
    def generate_jwt(id):
        now = datetime.datetime.utcnow()
        payload = {"user_id": id, "exp": now + datetime.timedelta(days=1), "iat": now}

        return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
