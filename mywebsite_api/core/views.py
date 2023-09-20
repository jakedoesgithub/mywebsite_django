from .serializers import ContactSerializer
from django.http import JsonResponse
from json import JSONDecodeError
from rest_framework.parsers import JSONParser
from rest_framework.views import views, status
from rest_framework.response import Response


class ContactAPIView(views.APIView):
    """
    Simple API view for contact entries
    """

    serializer_class = ContactSerializer

    def get_serializer_context(self) -> dict:
        """Get the serializer context.

        Returns:
            dict: The serializer context
        """
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs) -> ContactSerializer:
        """Get the serializer.

        Returns:
            ContactSerializer: The serializer
        """
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request) -> Response:
        """Handle POST requests.

        Args:
            request (Request): The request

        Returns:
            Response: The response
        """
        try:
            data = JSONParser().parse(request)
            serializer = ContactSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST
            )
