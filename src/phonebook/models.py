from django.db import models

class Persone(models.Model):
    name = models.CharField("Contact name", max_length=70)
    def __str__(self):
        return self.name
    
    def all_phones_to_string(self):
        return ", ".join([phone.phone for phone in self.phones.all()])


class Phone(models.Model):
    phone = models.CharField(
        verbose_name="Phone",
        max_length=12
    )
    contact = models.ForeignKey(
        Persone,
        related_name="phones",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.phone
    