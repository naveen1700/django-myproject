from django.db import models

class Contact(models.Model):
    name  = models.CharField(max_length=122)
    phone = models.CharField(max_length=15)        # 10–15 digits is enough
    email = models.EmailField(max_length=254)      # proper email field
    desc  = models.TextField()
