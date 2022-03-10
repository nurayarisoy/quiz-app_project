# from asyncore import write
# from dataclasses import fields
# import email
from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
 
class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required = True,
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type" : "password"} #password acik sekilde yazilmiyor
    )
    
    
    class Meta:
        model = User
        fields = [            
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {
            'password': {'write_only' : True},
            'password2': {'write_only' : True},
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password" : "Password fields didn't match."}
            )
        return data



class UserTokenSerializer(serializers.ModelSerializer):

    class Meta:
        Model=User
        Fields=('id','first_name','last_name','email')

class customTokenSerializer(TokenSerializer):
    
    user= UserTokenSerializer(read_only=True)

    
    class meta (TokenSerializer.Meta):
              fields=('key','user')