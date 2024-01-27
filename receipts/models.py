from django.db import models
from django.core.validators import RegexValidator
import uuid

# Regex validator for monetary values
currency_regex_validator = RegexValidator(regex=r'^\d+\.\d{2}$',
                                          message="Value must be in the format '123.45'")

class Purchase(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    retailer = models.CharField(max_length=100)
    purchaseDate = models.DateField()
    purchaseTime = models.TimeField()
    total = models.CharField(max_length=10, validators=[currency_regex_validator])

    def __str__(self):
        return str(self.uuid)

class Item(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='items', on_delete=models.CASCADE)
    shortDescription = models.CharField(max_length=200)
    price = models.CharField(max_length=10, validators=[currency_regex_validator])

    def __str__(self):
        return self.shortDescription