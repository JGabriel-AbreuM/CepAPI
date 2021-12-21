from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pycep_correios import get_address_from_cep, exceptions

def validaCPF(valor):
    try:
        get_address_from_cep(valor)
        
    except exceptions.InvalidCEP as eic:
        raise ValidationError(_('%(value)s CEP inválido'), params={'value': eic},) 

    except exceptions.CEPNotFound as ecnf:
        raise ValidationError(_('%(value)s CEP não encontrado'), params={'value': ecnf},)

    except exceptions.ConnectionError as errc:
        raise ValidationError(_('%(value)s Erro de conexão'), params={'value': errc},)

    except exceptions.Timeout as errt:
        raise ValidationError(_('%(value)s'), params={'value': errt},)

    except exceptions.HTTPError as errh:
        raise ValidationError(_('%(value)s'), params={'value': errh},)

    except exceptions.BaseException as e:
        raise ValidationError(_('%(value)s'), params={'value': e},) 