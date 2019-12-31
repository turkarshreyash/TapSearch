# Shreyash H. Turkar
# 31 December 2019

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from . import textpreprocessor
from . import models
from django.urls import reverse
import os
import PyPDF2
import re
import concurrent.futures
from django.conf import settings
# Create your views here.


def home(request):
    return render(request, "wordsearch/home.html")


# function for adding paragraphs
def feedpara(request):
    # get the text from post request
    long_string = request.POST["long_string"]

    # extract paragraphs
    paragraphs = textpreprocessor.getParagraphs(long_string)

    # process each paragrap
    for i in paragraphs:
        # store this paragraph in data base
        new_paragraph = models.Paragraphs(text=i)
        new_paragraph.save()

        # extract words by preprocessing
        words = textpreprocessor.textPreprocessor(i)

        # store all words in database
        for j in words:
            # store word if not exist
            new_word, added = models.Words.objects.get_or_create(word=j)
            # link word and para via word_para table
            new_index = models.word_para(
                word_id=new_word, para_id=new_paragraph)
            new_index.save()

    return HttpResponseRedirect(reverse('wordsearch:home'))


# for pdf files
def feedpdf(request):
    myfile = request.FILES['file']

    #File System
    fs = FileSystemStorage()

    #save the file
    filename = fs.save(myfile.name, myfile)

    #get url of the file
    uploaded_file_url = fs.url(filename)
     
    #get url + base dir
    file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file_url)

    #save pdf 
    pdf_file = models.PDFStorage(url=str(file_path))
    pdf_file.save()

    #text extraction from pdf
    pdfFileObj = open(pdf_file.url, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    #for each pages
    no_of_pages = pdfReader.numPages
    for i in range(no_of_pages):

        pageObj = pdfReader.getPage(i)
        words = re.findall("[a-zA-Z]+",pageObj.extractText().lower())
       
        #store each words
        for j in words:
            # store word if not exist
            new_word, added = models.Words.objects.get_or_create(word=j)
            # link word and para via word_para table
            new_index = models.word_pdf(word_id=new_word, pdf_id=pdf_file)
            new_index.save()

    return HttpResponseRedirect(reverse('wordsearch:home'))


# function for searching paragraphs
def search(request):

    # extract the word from post request
    word = request.POST["word"].lower()

    #parametres to pass to the templates
    results = dict()

    # find word in Words DB
    try:
        word = models.Words.objects.get(word__exact=word)
    except:
        word = None
        
    # if exist find in paragraph
    if word:
        
        #search in pdf and para parallely
        #executor for threads
        executor = concurrent.futures.ThreadPoolExecutor()

        #thread for paragraphs
        t1 = executor.submit(textpreprocessor.searchParagraphs,word)
        
        #thread for pdfs
        t2 = executor.submit(textpreprocessor.searchPDF,word)

        #get results
        pararesults = t1.result()
        pdfresults = t2.result()

        #added to final parameters
        results.update(pararesults)
        results.update(pdfresults)

    return render(request, "wordsearch/search.html", results)

def download(request, path=""):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("Not FOund")




# function for deleting database enters
def clear(request):
    models.Paragraphs.objects.all().delete()
    models.word_para.objects.all().delete()
    models.Words.objects.all().delete()
    models.PDFStorage.objects.all().delete()
    models.word_pdf.objects.all().delete()
    return HttpResponseRedirect(reverse('wordsearch:home'))
