from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . serializers import UserRegistrationSerializer
from . validators import custom_validation,validate_email,validate_password,validate_username



class UserRegistrationView(APIView):
#   renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    data = custom_validation(request.data)
    print(data)
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
    # token = get_tokens_for_user(user)
        return Response({ 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    return Response({ 'msg':'Registration Successful'}, status=status.HTTP_400_BAD_REQUEST)

