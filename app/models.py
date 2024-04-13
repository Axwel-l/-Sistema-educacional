from django.db import models

# Create your models here.
class Docente(models.Model):
    nome = models.CharField(
        unique=True,
        max_length=80,
    )
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.nome = self.nome.upper()
        
        super(Docente,self).save(*args,**kwargs)


class Aluno(models.Model):
    nome = models.CharField(
        unique=True,
        max_length=80,
    )
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.nome = self.nome.upper()
        
        super(Aluno,self).save(*args,**kwargs)

class Disciplina(models.Model):
    nome = models.CharField(
        unique=True,
        max_length=80,
    )
    data_criacao = models.DateField()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.nome = self.nome.upper()
        
        super(Disciplina,self).save(*args,**kwargs)
