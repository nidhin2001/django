from rest_framework import serializers
from .models import user
class Userserializer(serializers.ModelSerializer):
    class meta:
        model=user
        fields=['id','name','email','password']
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        password= validated_data.pop('password', None)
        instance=self.meta.model(**validated_data)
        if password is not None:
            instance.save()
            return instance
