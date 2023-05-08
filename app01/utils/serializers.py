from rest_framework import serializers
from app01 import models


class MyUserSerializers(serializers.Serializer):
    user = serializers.CharField()
    password = serializers.CharField()
    xxx = serializers.CharField(source="get_permissions_display")


class MyTokenSerializers(serializers.Serializer):
    yyy = serializers.CharField(source='user.password')
    token = serializers.CharField()


class MyUserModelSerializers(serializers.ModelSerializer):
    level = serializers.CharField(source='get_permissions_display')

    class Meta:
        model = models.User
        fields = ['user', 'password', 'level']
        # 连表操作
        # fields = '__all__'
        # depth = 1


class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class MyUserModelSerializers2(serializers.ModelSerializer):
    uu = serializers.HyperlinkedIdentityField(view_name='gp')

    class Meta:
        model = models.User
        fields = ['user', 'password', 'uu']


class MyVerifySerializers(serializers.Serializer):
    context = serializers.CharField(error_messages={'required:': '内容不能为空'})
