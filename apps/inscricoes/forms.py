#coding:utf-8
from django import forms
from django.contrib.localflavor.br.forms import BRPhoneNumberField,BRCPFField, BRZipCodeField
from models import Inscricoes, Palestras

class InscricoesForm(forms.ModelForm):
    cpf = BRCPFField(label="CPF*", help_text="Entre com um CPF válido")
#    cep = BRZipCodeField(label="CEP*", help_text="<html><a href=http://www.google.com>google</a> </html>")

    class Meta:
        model = Inscricoes
