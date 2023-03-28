import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    class Meta:
        abstract = True

class Servico(Base):
    
    ICONE_CHOICES = (
        ('lni-cog','Engrenagem'),
        ('lni-stats-up','Gráfico'),
        ('lni-users','Usuários'),
        ('lni-layers','Design'),
        ('lni-mobile','Mobile'),
        ('lni-rocket','Foguete'),
    )
    
    servico = models.CharField('Serviço', max_length=120)
    descricao = models.TextField('Descrição', max_length=250)
    icone = models.TextField('Icone', max_length=12, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self) -> str:
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo',max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self) -> str:
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome',max_length=120)
    cargo = models.ForeignKey('core.Cargo',verbose_name='cargo',on_delete=models.CASCADE)
    bio = models.TextField('Bio',max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':480,'height':480, 'crop':True}}) #crop - corte
    facebook = models.CharField('Facebook',max_length=120,default='#') 
    twitter = models.CharField('Twitter',max_length=120,default='#') 
    instagram = models.CharField('Instagram',max_length=120,default='#')
    
    class Meta:
        verbose_name = 'Funcionário' 
        verbose_name_plural = 'Funcionários'
        
    def __str__(self) -> str:
        return self.nome 
    
class Recurso(Base):
    
    ICONE_CHOICES = (
        ('lni-cog','Engrenagem'),
        ('lni-rocket','Foguete'),
        ('lni-laptop-phone','Dispositivos'),
        ('lni-leaf','Folha'),
        ('lni-layers','papel'),
    )
    recurso = models.CharField('Nome',max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.TextField('Icone', max_length=16, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
    
    def __str__(self):
        return self.recurso