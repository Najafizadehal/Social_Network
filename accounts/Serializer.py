from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()
class RegisterSerializer(serializers.models):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.object.all())]
    )

    class Meta:
        model = User
        fields = (
            'email','username','password_1', 'password_2',
            'first_name', 'last_name'
        )

        extra_kwargs = {
            'first_name':{'required':False},
            'last_name':{'required':False}
        }

        def Validator(self, attr):
            if attr['password_1'] != attr['password_2']:
                raise serializers.ValidationError({
                    'password' : 'password did not match.'
                })
            return attr

        def create(self, validate_data):
            user = User.object.create(
                username = validate_data['username'],
                email = validate_data['email'],
                first_name = validate_data.get('first_name',''),
                last_name = validate_data.get('last_name','')
            )

            user.set_password(validate_data['password_1'])
            user.save()



