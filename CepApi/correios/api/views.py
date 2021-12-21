from correios.models import Endereco
from .serializers import RegisterEndereco, EnderecoSerializer
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from django.urls import reverse_lazy
from pycep_correios import get_address_from_cep, exceptions

class CreateEndereco(generics.GenericAPIView):
    serializer_class = RegisterEndereco

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "Data": EnderecoSerializer(user, context=self.get_serializer_context()).data,
            }
        )


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ['get', 'head', 'put']
