from django.test import TestCase
from linguas.models import Lingua
from termos.models import Termo


class TermoModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        lingua = Lingua.objects.create(codigo='codigo', descricao='descricao teste')
        Termo.objects.create(lingua=lingua, texto='texto test')

    def test_lingua_label(self):
        termo = Termo.objects.get(id=1)
        lingua_label = termo._meta.get_field('lingua').verbose_name
        self.assertEquals(lingua_label, 'lingua')

    def test_texto_label(self):
        termo = Termo.objects.get(id=1)
        texto_label = termo._meta.get_field('texto').verbose_name
        self.assertEquals(texto_label, 'texto')
