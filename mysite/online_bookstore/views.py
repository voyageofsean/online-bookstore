from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, User, ShoppingCart, Order
from random import sample
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
            ISBN=sheet.cell(i, 0),
            BookName=sheet.cell(i, 1),
            BookAuthor=sheet.cell(i, 2),
            BookNum=sheet.cell(i, 3),
            BookPrice=sheet.cell(i, 4),
            PublishDate=sheet.cell(i, 5),
            ShelfDate=sheet.cell(i, 6),
            information=sheet.cell(i, 7))


# 注册功能
def register(request):
    # 定义一个错误提示为空
    error_name = ''
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_list = User.objects.filter(UserName=user)
        if user_list:
            # 注册失败
            error_name = '%s用户名已经存在了' % user
            # 返回到注册页面，并且把错误信息报出来
            return render(request, 'register.html', {'error_name': error_name})
        else:
            # 数据保存在数据库中，并返回到登录页面
            user = User.objects.create(UserName=user,
                                       UserKey=password,
                                       UserAddress=email)
            user.save()
            return redirect('/online_bookstore/login/')

    return render(request, 'register.html')


# 登录功能
def login(request):
    # 定一个为空的错误接收
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 判断数据库中有没有账号密码
        ret = User.objects.filter(UserName=username, UserKey=password)
        if ret:
            # 登录到主界面
            return redirect('/online_bookstore/')
        else:
            # 登录失败
            error_msg = '用户名或密码错误，请重新输入！'
    return render(request, 'login.html', {'error_msg': error_msg})


# 书籍查询功能
def search(request):
    error_msg = ''
    if request.method == 'POST':
        query = request.POST.get('q')
        # 查询所有可能结果
        book_list = (Book.objects.filter(ISBN__icontains=query) | Book.objects.filter(
            BookName__icontains=query) | Book.objects.filter(BookAuthor__icontains=query)).distinct()
        if not book_list:
            error_msg = '没找到所需的书籍'
        return render(request, 'search.html', {'error_msg': error_msg, 'book_list': book_list})
    return render(request, 'search.html', {'error_msg': error_msg})


# 书籍详细信息功能
def information(request, isbn):
    book = Book.objects.filter(ISBN=isbn)
    return render(request, 'information.html', {'book': book})


# 书籍展示功能 随机推荐k本书籍
def display(request):
    ####选择随机推荐的书籍数####
    k = 1
    ###########################
    book_list = Book.objects.all()
    count = book_list.count()
    rand_ids = sample(range(0, count), k)
    selected_list = []

    for i in rand_ids:
        selected_list.append(book_list[i])

    return render(request, 'display.html', {'books': selected_list})
