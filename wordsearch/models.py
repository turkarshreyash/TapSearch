from django.db import models

# Create your models here.
class Paragraphs(models.Model):
    text = models.TextField()

class Words(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word

class word_para(models.Model):
    word_id = models.ForeignKey(Words,on_delete=models.CASCADE)
    para_id = models.ForeignKey(Paragraphs,on_delete=models.CASCADE)

class PDFStorage(models.Model):
    url = models.CharField(max_length=255)


class word_pdf(models.Model):
    word_id = models.ForeignKey(Words,on_delete=models.CASCADE)
    pdf_id = models.ForeignKey(PDFStorage,on_delete=models.CASCADE)