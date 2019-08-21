from helloworld.models import Produto, Foo
from django import forms

# FORMULÁRIO DE SELEÇÃO DE ARQUIVOS DE TEXTO
# -------------------------------------------

class SelecionaTexto(forms.ModelForm):


    class Meta:
        # Modelo base
        model = Foo



        # Campos que estarão no form
        fields = [
            'audio'
        ]


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereProdutoForm(forms.ModelForm):


    class Meta:
        # Modelo base
        model = Produto



        # Campos que estarão no form
        fields = [
            'questao_de_pesquisa',
            'metodo',
            'aplicacao_metodo',
            'tipo_dado',
            'qtde_dado',
            'metodo_analise',
            'natureza_resultado',
            'dados_justifica'
        ]
