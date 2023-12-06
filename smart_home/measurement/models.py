from django.db import models

class Sensor(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=150)

    class Meta:
        verbose_name='Датчик'
        verbose_name_plural = 'Датчики'

    def  __str__(self):
        return f'{self.name}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor,on_delete=models.CASCADE,related_name='measurements')
    temperature = models.DecimalField(max_digits=5,decimal_places=1)
    datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor}'

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
