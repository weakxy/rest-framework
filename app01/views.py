import json
import time
import hashlib
from django.views import View
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from app01.utils.auth import MyAuthentication
from app01.utils.permissions import MyPermission
from app01.utils.versioning import MyUrlVersion, MyBaseVersion, MyQueryVersion
from app01 import models
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.parsers import JSONParser, FormParser


def md5(user):
    ctime = str(time.time())

    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


def sign_in(request):
    return HttpResponse("注册成功")


class CBV(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class DogView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        self.dispatch
        ret = {
            'code': 1000,
            'msg': 'xxx',
        }
        return HttpResponse(json.dumps(ret), status=201)

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request._request.POST.get('user')
            pwd = request._request.POST.get('password')
            obj = models.User.objects.filter(user=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '错误'
            token = md5(user)
            print(token)
            models.UserOrder.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            pass
        return JsonResponse(ret)


class OrderPayment(APIView):
    # authentication_classes = [MyAuthentication, ]
    # permission_classes = [MyPermission, ]

    def get(self, request, *args, **kwargs):
        self.dispatch
        ret = {
            'code': 1000,
            'msg': 'xxx',
        }
        return HttpResponse(json.dumps(ret), status=201)

    def post(self, request, *args, **kwargs):
        pass


class UsersView(APIView):
    # versioning_class = MyBaseVersion
    # versioning_class = MyQueryVersion
    # versioning_class = MyUrlVersion

    def get(self, request, *args, **kwargs):
        print(request.version)
        return HttpResponse("OKOK")


from rest_framework.parsers import JSONParser, FormParser


class ParserView(APIView):
    parser_classes = [JSONParser, FormParser]
    """
    JSONParser能解析头'application/json'
    FormParser能解析头'application/x-www-form-urlencoded'
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse("eiphier")

    def post(self, request, *args, **kwargs):
        print(request.data)
        return HttpResponse("weakxy")


from app01.utils.serializers import MyUserSerializers, MyTokenSerializers, MyUserModelSerializers, \
    MyUserModelSerializers2, MyVerifySerializers


class SerializersView(APIView):

    def get(self, request, *args, **kwargs):
        user_datas = models.User.objects.all()
        token_datas = models.UserOrder.objects.all()
        # user_result = MyUserSerializers(instance=user_datas, many=True)
        user_result = MyUserModelSerializers(instance=user_datas, many=True)
        token_result = MyTokenSerializers(instance=token_datas, many=True)
        user_result = json.dumps(user_result.data, ensure_ascii=False)
        token_result = json.dumps(token_result.data, ensure_ascii=False)
        return HttpResponse(user_result, token_result)

    def post(self, request, *args, **kwargs):
        pass


class Serializers2View(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = models.User.objects.filter(id=pk)
        obj_result = MyUserModelSerializers2(instance=obj, many=True, context={'request': request})
        obj_result = json.dumps(obj_result.data, ensure_ascii=False)
        print(obj_result)
        return HttpResponse(obj_result)

    def post(self, request, *args, **kwargs):
        pass


class SerializerVerify(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        ser = MyVerifySerializers(data=request.data)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)

        return HttpResponse('提交数据')


from app01.utils.pager import MyPager
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class PagerView(APIView):
    def get(self, request, *args, **kwargs):
        self.dispatch
        obj = models.User.objects.all()

        pg = PageNumberPagination()
        page_role = pg.paginate_queryset(queryset=obj, request=request, view=self)
        ser = MyUserModelSerializers(instance=page_role, many=True)

        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        pass


from rest_framework.generics import GenericAPIView
from app01.utils.serializers import PageSerializers
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class View(ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = PageSerializers
    pagination_class = PageNumberPagination
