from django.test import TestCase

from linguas.models import Lingua


class LinguaModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Lingua.objects.create(codigo='codigo', descricao='descricao')

    def test_codigo_label(self):
        lingua = Lingua.objects.get(codigo='codigo')
        codigo_label = lingua._meta.get_field('codigo').verbose_name
        self.assertEquals(codigo_label, 'codigo')

    def test_descricao_label(self):
        lingua = Lingua.objects.get(codigo='codigo')
        descricao_label = lingua._meta.get_field('descricao').verbose_name
        self.assertEquals(descricao_label, 'descricao')

    def test_str(self):
        lingua = Lingua.objects.get(codigo='codigo')
        lingua_str = str(lingua)
        self.assertEquals(lingua_str, lingua.codigo)
