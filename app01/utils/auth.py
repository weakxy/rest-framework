from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from app01 import models


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = models.UserOrder.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user, token_obj)

    # 认证失败返回的响应头
    def authenticate_header(self, val):
        pass
