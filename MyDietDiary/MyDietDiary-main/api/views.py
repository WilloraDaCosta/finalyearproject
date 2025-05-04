from django.contrib.auth import authenticate
from rest_framework import status, views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import RecommendationSerializer, UserSerializer, Page1Serializer, Page2Serializer, Page3Serializer, Page4Serializer, Page5Serializer
from .models import UserData
from recommender.functions import Weight_Loss, Weight_Gain, Healthy  # Import functions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def get_recommendations(request):
    """
    API endpoint to get food recommendations based on user inputs.
    Expects JSON input: {"age": 25, "weight": 70, "height": 175, "goal": "weight_loss", "sleep_duration": 7, "quality_of_sleep": "Good", "physical_activity_level": "high", "stress_level": "high", "Blood_pressure_category": "Hypertension", "Heart_rate": 80, "Daily_steps" : 6000, "occupation": "Doctor"}
    """
    data = request.data
    age = data.get("age")
    weight = data.get("weight")
    height = data.get("height")
    goal = data.get("goal", "weight_loss")  # Default to weight loss

    if not all([age, weight, height]):
        return Response({"error": "Missing required parameters"}, status=400)

    # Call the appropriate function
    if goal == "weight_loss":
        recommendations = Weight_Loss(age, weight, height)
    elif goal == "weight_gain":
        recommendations = Weight_Gain(age, weight, height)
    elif goal == "healthy":
        recommendations = Healthy(age, weight, height)
    else:
        return Response({"error": "Invalid goal. Use 'weight_loss', 'weight_gain', or 'healthy'."}, status=400)

    # Check if recommendations contain required fields
    if not recommendations or "bmi" not in recommendations or "bmi_info" not in recommendations:
        return Response({"error": "No food recommendations found."}, status=400)

    # Serialize the response correctly
    serializer = RecommendationSerializer(recommendations)
    return Response(serializer.data)

def login_user(request):
    """
    Login API for React Native app.
    Expects JSON: { "username": "user", "password": "pass" }
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Login successful',
            'user': user.username,
            'token': token.key  # 🔑 THIS is what your frontend needs
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

# def sleep_data(request):
#     serializer = SleepDataSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

@permission_classes([AllowAny])
class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        # Validate incoming data using the serializer
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # Save the new user if the data is valid
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username}, status=201)
          #  return Response({"message": "User created successfully!", "user_id": user.id}, status=status.HTTP_201_CREATED)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UserDataView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = UserDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response({'message': 'User data saved successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def get_or_create_userdata(user):
    userdata, created = UserData.objects.get_or_create(user=user)
    return userdata

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class Page1View(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        userdata = get_or_create_userdata(request.user)
        serializer = Page1Serializer(userdata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Page 1 data saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Page2View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        userdata = get_or_create_userdata(request.user)
        serializer = Page2Serializer(userdata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Page 2 data saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Page3View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        userdata = get_or_create_userdata(request.user)
        serializer = Page3Serializer(userdata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Page 3 data saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Page4View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        userdata = get_or_create_userdata(request.user)
        serializer = Page4Serializer(userdata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Page 4 data saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Page5View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        userdata = get_or_create_userdata(request.user)
        serializer = Page5Serializer(userdata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Page 5 data saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)