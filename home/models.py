from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, default="0")
    profil_image = models.ImageField(upload_to='images/', default='image.png', null=True ,blank=True)
    def __str__(self) -> str:
        return str(self.user)

# Create your models here.

class AccountModel(models.Model):
    turi=(
        ('garant account','garant account'),
        ('reseler account','reseler account')
    )
    level = models.CharField(max_length=50,default='1')
    
    price = models.IntegerField()
    rp = models.CharField(max_length=100,default='0')
    acount_image = models.ImageField(upload_to='profileimg/',default='defult_img')
    profil = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, null=True)
    turi = models.CharField(max_length=20, choices=turi, default=None)
    mifik = models.CharField(max_length=100,default='ok')
    qoshimcha = models.CharField(max_length=100,default='qoshimchalar')
    murojaat_uchun = models.CharField(max_length=100, default='+998')
    def __str__(self) -> str:
        return str(self.name)
    

def  create_profil(sender,instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(
            user=instance
        )
    else:
        profilemodel = ProfileModel.objects.get(user=instance)
        profilemodel.email = instance.email
        profilemodel.name = f"{instance.first_name} {instance.last_name}"
        profilemodel.save()
        
Signal.connect(post_save,create_profil,sender=User)

