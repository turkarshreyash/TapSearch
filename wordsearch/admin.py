from django.contrib import admin
from .models import Paragraphs, Words, word_para, PDFStorage, word_pdf

# Register your models here.



admin.site.register(Paragraphs)
admin.site.register(Words)
admin.site.register(word_para)
admin.site.register(PDFStorage)
admin.site.register(word_pdf)