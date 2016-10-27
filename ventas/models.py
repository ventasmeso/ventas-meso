from django.db import models
#from django.utils import timezone

class Producto(models.Model):    
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    existencias = models.IntegerField()
    #imagen = models.ImageField()

    #def publish(self):
        #self.published_date = timezone.now()
        #self.save()
    
    def __str__(self):
        return self.nombre