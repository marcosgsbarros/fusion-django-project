from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):
    
    def setUp(self):
        self.nome = 'Marcos'
        self.email = 'marcosgsbarros@gmail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem qualquer'
    
        self.dados = {
            'nome':self.nome,
            'email':self.email,
            'assunto':self.assunto,
            'mensagem':self.mensagem,          
            }
        
        self.form = ContatoForm(data=self.dados)
        
    def test_send_mail(self):
        form = ContatoForm(data=self.dados)
        form.is_valid()
        envia1 = form.send_mail()
        
        form2 = self.form
        form2.is_valid()
        envia2 = form2.send_mail()
        
        self.assertEquals(envia1,envia2)
        