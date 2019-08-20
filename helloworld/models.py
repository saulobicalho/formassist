from django.db import models


class Produto(models.Model):


    questao_de_pesquisa = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    metodo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    aplicacao_metodo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    tipo_dado = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    qtde_dado = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    metodo_analise = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    natureza_resultado = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    dados_justifica = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    objetos = models.Manager()
