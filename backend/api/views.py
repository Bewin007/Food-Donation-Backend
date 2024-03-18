from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Donate_food, Donate_Grocery, Request
from .serializers import CustomUserSerializer, DonateFoodSerializer, DonateGrocerySerializer, RequestSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class GETCustomUserAPIView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)






class GETDonateFoodAPIView(APIView):
    def get(self, request):
        donations = Donate_food.objects.filter(status= True)
        serializer = DonateFoodSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonateFoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GETDonateGroceryAPIView(APIView):
    def get(self, request):
        donations = Donate_Grocery.objects.filter(status= True)
        serializer = DonateGrocerySerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonateGrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GETRequestAPIView(APIView):
    def get(self, request):
        requests = Request.objects.filter(status= True)
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            custom_data = {
                'id': user.id,
                'name':user.username,
                'email': user.email
            }

            refresh = RefreshToken.for_user(user)
            refresh['custom_data'] = custom_data  # Add custom data to the token payload
            refresh.access_token.payload['custom_data'] = custom_data  # Also add to the access token payload

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
    




class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = CustomUser.objects.get(username=username,password=password)
        print(user)
        if user:
            refresh = RefreshToken.for_user(user)

            custom_data = {
                'id': user.id,
                'name': user.username,
                'email': user.email
            }

            refresh['custom_data'] = custom_data
            refresh.access_token.payload['custom_data'] = custom_data

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class DonateFoodAPIView(APIView):

    def post(self, request):
        serializer = DonateFoodSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(id=request.data.get('donator'))
            user.donated+=1
            user.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DonateFoodReceveAPIVIEW(APIView):
    def patch(self, request):
        id = request.data.get('id')
        try:
            donation = Donate_food.objects.get(id=id, status=True)
        except Donate_food.DoesNotExist:
            return Response("Donation not found", status=404)
        

        donation.status = False
        donation.receiver = CustomUser.objects.get(id=request.data.get('recever'))
        donation.save()

        return Response('Donation updated successfully')

class DonateGroceryAPIView(APIView):
    def post(self, request):
        serializer = DonateGrocerySerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(id=request.data.get('donator'))
            user.donated+=1
            user.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DonateGroceryReceveAPIVIEW(APIView):
    def patch(self, request):
        id = request.data.get('id')
        try:
            donation = Donate_Grocery.objects.get(id=id, status=True)
        except Donate_Grocery.DoesNotExist:
            return Response("Donation not found", status=404)
        
        # user = request.data.get('id')
        donation.status = False
        donation.receiver = CustomUser.objects.get(id=request.data.get('recever'))
        donation.save()
        return Response('Donation updated successfully')


class RequestAPIView(APIView):
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(id=request.data.get('requestor'))
            user.requested+=1
            user.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestReceveAPIVIEW(APIView):
    def patch(self, request):
        id = request.data.get('id')
        try:
            donation = Request.objects.get(id=id, status=True)
        except Request.DoesNotExist:
            return Response("Donation not found", status=404)
        
        donation.status = False
        donation.receiver = CustomUser.objects.get(id=request.data.get('recever'))
        donation.save()
        return Response('Donation updated successfully')
