from django.db import models

class Persone(models.Model):
    name = models.CharField("Contact name", max_length=70)
    def __str__(self):
        return self.name


class Phone(models.Model):
    phones = models.TextField(
        verbose_name="Phones",
        help_text="Введите номера телефонов, каждый с новой строки"
    )
    contact = models.ForeignKey(
        Persone,
        related_name="phones",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.phone
    

