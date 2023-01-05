from django.db import models

# Create your models here.

class Kelompok(models.Model):
    kategori = models.CharField(max_length=40)
    keterangan = models.TextField()

    def __str__(self):
        return self.kategori

class Ikan(models.Model):
    nama = models.CharField(max_length=50)
    nama_ilmiah = models.CharField(max_length=50)
    img = models.CharField(max_length=30, null=True)
    detail = models.URLField(max_length=100, null=True)
    kelompok_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nama
