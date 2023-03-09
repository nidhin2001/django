from rest_framework.views import APIView
from .serializer import Userserializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import user
import jwt
import datetime
# Create your views here.
class registerview(APIView):
    def post(selfself, request):
        serializer= Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        User= user.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        payload ={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30),
            'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='hs256').decode('utf-8')

        res=Response()
        res.set_cookie(key='jwt',value=token,httponly=True)
        res.data={"jwt":token}
        return  res



class Userview(APIView):
    def get(self,request):
        token=request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed('unauthentication')
        try:
            payload=jwt.decode(token,'secret',algorithms=['hs256'])
            user1=user.objects.filter(id=payload['id'])
            serializer=Userserializer(user1)
        return Response(token)

class logoutview(APIView):
    def post(self,request):
        res=Response()
        Response.delete_cookie('jwt')
        res.data={"message":"success"}
