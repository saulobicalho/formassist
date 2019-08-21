from django.db import models

class Produto(models.Model):


    questao_de_pesquisa = models.TextField(
        max_length=255,
        null=False,
        blank=False,
        help_text="(Que perguntas se quer responder com o método?)"
    )

    metodo = models.TextField(
        max_length=255,
        null=False,
        blank=False,
        help_text="(Nome dos métodos aplicados)"
    )

    aplicacao_metodo = models.TextField(
        max_length=255,
        null=False,
        blank=False,
        help_text="(Decisões relacionadas ao modo como o método foi aplicado)"
    )

    tipo_dado = models.TextField(
        max_length=255,
        null=False,
        blank=False
    )

    qtde_dado = models.TextField(
        max_length=255,
        null=False,
        blank=False
    )

    metodo_analise = models.TextField(
        max_length=255,
        null=False,
        blank=False
    )
    natureza_resultado = models.TextField(
        max_length=255,
        null=False,
        blank=False
    )
    dados_justifica = models.TextField(
        max_length=255,
        null=False,
        blank=False
    )

    objetos = models.Manager()
