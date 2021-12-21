from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from correios.models import Endereco
from pycep_correios import get_address_from_cep, exceptions


class RegisterEndereco(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ["cep"]

    def create(self, validated_data):
        dict_local = get_address_from_cep(validated_data["cep"])

        novo_endereco = Endereco.objects.create(
            bairro = dict_local["bairro"],
            cep = dict_local["cep"],
            cidade = dict_local["cidade"],
            logradouro = dict_local["logradouro"],
            uf = dict_local["uf"],
        )

        return novo_endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ("id", "bairro", "cep", "cidade", "logradouro", "uf")