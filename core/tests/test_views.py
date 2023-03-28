from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        
        self.dados = {
            'nome':'marcos',
            'email':'marcos@gmail.com',
            'assunto':'teste de assunto',
            'mensagem':'teste de mensagem'
            
        }
        cliente = Client()
    
    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'),data=self.dados)
        self.assertEquals(request.status_code,302)
    
    def test_form_invalid(self):
        dados = {
            'nome':'marcos',
            'email':'email'
        }
        request = self.client.post(reverse_lazy('index'),data=dados)
        self.assertEquals(request.status_code,200)
    