# from django.db import models

# # Create your models here.
# class CrudUser(models.Model):
#     name = models.CharField(max_length=30, blank=True)
#     address = models.CharField(max_length=100, blank=True)
#     age = models.IntegerField(blank=True, null=True)
#     class Meta:
#         ordering = ['-name']
#         indexes = [
#             models.Index(fields=['name',]),
            
#         ]
#     def __str__(self):
#         return '%s %s' % (self.id, self.name)
