from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        return render(request, 'Clone_coding/main.html')