from django.db import models

class Skin(models.Model):
    """Modelo de Skin do Counter Strike"""

    """ Nome do armamento """
    arma = models.CharField(max_length=30, blank=False, default='')
    
    """ Nome da skin """
    nome = models.CharField(max_length=30, blank=False, default='')
    
    """ Preço da skin """
    preco = models.IntegerField()
    
    """ Float de desgaste """
    float = models.FloatField()
    
    """ Nomeação do degaste """
    desgaste = models.CharField(max_length=30)
    
    """ Se a arma esta adesivada """
    adesivado = models.BooleanField(default=False)
    
    """ User do dono da skin """
    proprietario = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['nome']