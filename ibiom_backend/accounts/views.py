from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . serializers import UserRegistrationSerializer,UserProfileSerializer
from . validators import custom_validation,validate_password,validate_logincred
from django.contrib.auth import authenticate
from .managers import AccountsManager
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
account_manager = AccountsManager()

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }
  
class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    data = custom_validation(request.data)
    print(data)
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({ 'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    return Response({ 'msg':'Registration Successful'}, status=status.HTTP_400_BAD_REQUEST)


class TestView(APIView):
    
    def get(self,request):
        
        return Response({ 'msg':'Communication Successful'}, status=status.HTTP_201_CREATED)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        login_cred = validate_logincred(request.data.get('login_cred'))
        password = request.data.get('password')
        user = account_manager.authenticate(request , login_cred=login_cred, password=password)    
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
            

