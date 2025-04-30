from django.contrib.auth import authenticate
from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RecommendationSerializer
from recommender.functions import Weight_Loss, Weight_Gain, Healthy  # Import functions

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
    Expects JSON: { "emailOrUsername": "user", "password": "pass" }
    """
    email_or_username = request.data.get('emailOrUsername')
    password = request.data.get('password')

    if not email_or_username or not password:
        return Response({'error': 'Please provide both username/email and password'}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate using username (email-based login requires custom logic)
    user = authenticate(username=email_or_username, password=password)

    if user is not None:
        return Response({'message': 'Login successful', 'user': user.username}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)