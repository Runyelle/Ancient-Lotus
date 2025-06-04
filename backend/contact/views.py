from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from ratelimit.decorators import ratelimit
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@ratelimit(key='ip', rate='5/h', block=True)
def health_check(request):
    return JsonResponse({"status": "Backend is working!"})


class ContactView(APIView):
    renderer_classes = [JSONRenderer]
    
    def get(self, request):
        return HttpResponse("This endpoint only supports POST requests.")

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        full_message = f"From: {name} <{email}>\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)