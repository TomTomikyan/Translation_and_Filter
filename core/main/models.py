from django.db import models

# Create your models here.

class Qaxaq(models.Model):

    name = models.CharField('qaxaqi anun',max_length=50)
    img = models.ImageField('nkary',upload_to='qaxaqner')

    def __str__(self) -> str:
        return self.name

class Mayla(models.Model):

    Qaxaq = models.ForeignKey(Qaxaq,on_delete=models.CASCADE,related_name='Mayla')
    name = models.CharField('Mayla',max_length=50)
    img = models.ImageField('Mayli nkary',upload_to='Mayla',null=True)

    def __str__(self) -> str:
        return self.name

class Poxoc(models.Model):

    Mayla = models.ForeignKey(Mayla,on_delete=models.CASCADE,related_name='Poxoc')
    name = models.CharField('poxoci anun',max_length=50)
    img = models.ImageField('poxoci nkar',upload_to='poxoc',null=True)

    def __str__(self) -> str:
        return self.name