from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.CharField(max_length = 200, null=False, blank = False)
    price=models.FloatField(validators=[MinValueValidator(0)],null=False)
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default = 0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title