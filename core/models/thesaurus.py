from djongo import models

class Thesaurus(models.Model):
    data = models.JSONField()

    def __str__(self):
        return f'Thesaurus {self.id}'