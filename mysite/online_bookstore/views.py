from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import xlrd


def index(request):
    return HttpResponse("try try see")


def insert_book():
    books_info = xlrd.open_workbook('book.xls')
    sheet = books_info.sheet_by_index(1)
    nrows = sheet.nrows
    for i in range(nrows):
        Book.objects.create(
            ISBN = sheet.cell(i,0),
            BookName = sheet.cell(i,1),
            BookAuthor = sheet.cell(i,2),
            BookNum = sheet.cell(i,3),
            BookPrice = sheet.cell(i,4),
            PublishDate = sheet.cell(i,5),
            ShelfDate = sheet.cell(i,6),
            BookInformation = sheet.cell(i,7))