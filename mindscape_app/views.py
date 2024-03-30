# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserRegistrationSerializer

class UserRegistrationViewSet(viewsets.ViewSet):
    serializer_class = UserRegistrationSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Save the user to the database
            serializer.save()
            return Response({'success': 'User registered successfully'})
        else:
            return Response(serializer.errors, status=400)
