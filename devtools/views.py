from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DevToolSerializer
from .models import DevTool
from drf_yasg.utils import swagger_auto_schema

from typing import Any

# Create your views here.

class DevToolList(APIView):
    """
    This view handles listing all tools and creating a new tool
    """
    def get(self, request: Any) -> Response:
        """
        Handles getting all tools in the database or raises exception.
        """

        tools = DevTool.objects.all()
        serializer = DevToolSerializer(tools, many = True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body = DevToolSerializer)
    def post(self, request: Any) -> Response:

        """
        Handles creating a new tool in the database
        """
        serializer = DevToolSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DevToolDetail(APIView):
    """
    Handles retrieving, updating and deleting a single tool.
    """

    def get_object(self, pk: int) -> DevTool | None:
        """
        Helper method to get a DevTool object by it's primary key
        """
        try:
            return DevTool.objects.get(pk = pk)
        except DevTool.DoesNotExist:
            return None

    def get(self, request: Any, pk: int) -> Response:
        """
        Retrieve a single tool based on it's primary key
        """
        tool = self.get_object(pk)
        if tool:
            serializer = DevToolSerializer(tool)
            return Response(serializer.data)
        return Response({"error": "DevTool not found"}, status = status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body = DevToolSerializer)
    def put(self, request: Any, pk: int) -> Response:
        """
        Update a particular tool
        """
        tool = self.get_object(pk)
        if tool:
            serializer = DevToolSerializer(tool, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({"error": "DevTool not found"}, status = status.HTTP_404_NOT_FOUND)

   # @swagger_auto_schema(request_body = DevToolSerializer)
    def delete(self, request: Any, pk: int) -> Response:
        """
        Delete a particular tool
        """
        tool = self.get_object(pk)
        if tool:
            tool.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response({"error": "DevTool not found"}, status = status.HTTP_404_NOT_FOUND)
