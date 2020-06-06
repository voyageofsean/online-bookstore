from Bookshop.models import *
from django.utils import timezone
import random
import hashlib
import sys
import xlrd
import xlwt
reload(sys)
sys.setdefaultencoding('utf-8')


def insert_book():
    books_info = xlrd.open_workbook('book.xls')
    sheet = readbook.sheet_by_index(1)
    nrows = sheet.nrows
    for i in range(nrows):
        Book.objects.create(
            ISBN = tabel.cell(i,0),
            BookName = tabel.cell(i,1),
            BookAuthor = tabel.cell(i,2),
            BookNum = tabel.cell(i,3),
            BookPrice = tabel.cell(i,4),
            PublishDate = tabel.cell(i,5),
            ShelfDate = tabel.cell(i,6),
            BookInformation = tabel.cell(i,7))