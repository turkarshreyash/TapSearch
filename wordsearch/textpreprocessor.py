# All functions required text preprocessing and tokenization are here!
import re
from . import models
from django.db.models import Count


def getParagraphs(long_string):
    #split at two line space
    return long_string.split("\r\n\r\n")

def textPreprocessor(paragraph):
    #lower, remove punctuations marks and split at spaces
    return re.findall("[a-zA-Z]+",paragraph.lower())

def searchParagraphs(word):

    #get top 10 paragraphs
    paras = models.word_para.objects.filter(word_id=word).values("para_id").annotate(dcount=Count('para_id')).order_by('-dcount')[:10]

    #dict for final paras result
    para_results = dict()
    para_results["para"] = list()
    para_results["para_count"] = 0
    para_results["total_word_count"] = 0
    
    # for each paragraph
    for i in paras:

        # store number of times word occured it that para
        para_results["total_word_count"] += i["dcount"]
        para_results["para_count"] += 1

        # store text of para
        para_results["para"].append((models.Paragraphs.objects.get(id=i["para_id"]).text,i["dcount"]))

    return para_results

def searchPDF(word):

    #get pdfs
    paras = models.word_pdf.objects.filter(word_id=word).values("pdf_id").annotate(dcount=Count('pdf_id')).order_by('-dcount')[:10]

    #dict for final pdf result
    pdf_results = dict()
    pdf_results["pdf"] = list()
    pdf_results["pdf_count"] = 0
    pdf_results["pdf_total_word_count"] = 0
    
    # for each pdf
    for i in paras:

        # store number of times word occured it that pdf
        pdf_results["pdf_total_word_count"] += i["dcount"]
        pdf_results["pdf_count"] += 1

        # store url of pdf
        pdf_results["pdf"].append((models.PDFStorage.objects.get(id=i["pdf_id"]).url,i["dcount"]))

    return pdf_results