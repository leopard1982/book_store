from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from myapp.forms import BookForm, UploadMasterBookForm
from myapp.models import Books, UploadBookXLS
from django.conf import settings
import os
import pandas as pd

# Create your views here.


def homepage(request):
    mybook = Books.objects.all()
    return render(request, 'viewbook.html', {'data': mybook})


def masterBook(request):
    if request.method == "POST":
        forms = BookForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/master/book/')
    forms = BookForm()
    uploadform = UploadMasterBookForm()
    return render(request, 'masterbook.html', {'forms': forms, 'uploadform': uploadform})


def masterViewBook(request):
    mydata = Books.objects.all()
    return render(request, 'viewbook.html', {'mydata': mydata})


def masterUploadBook(request):
    if request.method == "POST":
        forms = UploadMasterBookForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
    return HttpResponseRedirect('/baca/')


def baca(request):
    filesnya = UploadBookXLS.objects.all().order_by("-id")[0]
    realfile = os.path.join(settings.BASE_DIR, "media\\" + str(filesnya.files))
    newdata = pd.read_excel(realfile)
    headers = []
    for col in newdata.columns:
        headers.append(col)

    for index, row in newdata.iterrows():
        if (row[0] != "nan"):
            try:
                booknya = Books()
                booknya.book_id = row[0]
                booknya.title = row[1]
                booknya.author = row[2]
                booknya.publisher = row[3]
                booknya.isbn = int(row[4])
                booknya.category = row[5]
                booknya.language = row[6]
                booknya.year = int(row[7])
                booknya.book_audience = row[8]
                booknya.num_page = int(row[9])
                if row[10] == "Yes":
                    booknya.part_series = True
                else:
                    booknya.part_series = False
                booknya.order_of_book = int(row[11])
                booknya.version_number = int(row[12])
                booknya.price = float(row[13])
                booknya.description = row[14]
                booknya.cover = row[15]
                booknya.save()
            except:
                pass
    return render(request, 'baca.html', {'data': newdata})
