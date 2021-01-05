from django.test import TestCase
from linguas.models import Lingua
from termos.models import Termo


class TermoModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        lingua, created = Lingua.objects.create(codigo='codigo', descricao='descricao teste')
        Termo.objects.create(lingua=lingua, texto='texto test')

    def test_lingua_label(self):
        termo = Termo.object.get(id=1)
        lingua_label = termo._meta.get_field('lingua').verbose_name
