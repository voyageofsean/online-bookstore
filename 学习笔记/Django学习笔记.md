## Django学习笔记

### 1 Django应用的创建和使用

#### 1.1 Django项目的构成

一个空的Django项目：

```
mysite/
    manage.py  一个让你用各种方式管理 Django 项目的命令行工具。
    mysite/
        __init__.py  一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。
        settings.py  Django 项目的配置文件。
        urls.py  Django 项目的 URL 声明，就像你网站的“目录”。
        asgi.py  作为你的项目的运行在 ASGI 兼容的Web服务器上的入口。
        wsgi.py  作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。
```

#### 1.2 部署简易的服务器

在mysite/位置

```
python manage.py runserver
```

访问服务器： https://127.0.0.1:8000/

#### 1.3 创建应用

```
python manage.py startapp polls
```

目录结构：

```
polls/
    __init__.py
    admin.py  管理员
    apps.py
    migrations/  数据表的迁移的记录
        __init__.py
    models.py  模型代码
    tests.py  测试代码
    views.py  视图代码
```

#### 1.4 创建视图

- Django 中的视图的概念是「一类具有相同功能和模板的网页的集合」。
- 通常来说，一个视图的工作就是：从参数获取数据，装载一个模板，然后将根据获取的数据对模板进行渲染。
- 视图函数的执行结果只可能有两种：返回一个包含请求页面元素的 [`HttpResponse`](https://docs.djangoproject.com/zh-hans/3.0/ref/request-response/#django.http.HttpResponse)  对象，或者是抛出 [`Http404`](https://docs.djangoproject.com/zh-hans/3.0/topics/http/views/#django.http.Http404)  这类异常。

创建返回一个`HttpResponse`的视图：

```python
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

后面会有更多对视图的讲解。

#### 1.4 创建URL映射

- URLconf将一个 URL 映射到视图。

为了创建 URLconf，请在 polls 目录里新建一个 `urls.py`  文件。在其中键入

```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
```

在根 URLconf 文件中指定我们创建的 `polls.urls` 模块。

```python
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

- path函数将url，以及其中的参数解析出来，传入对应的视图函数中。name参数：你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。
- include函数允许引用其它 URLconfs。每当 Django 遇到 [`include()`](https://docs.djangoproject.com/zh-hans/3.0/ref/urls/#django.urls.include) 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。

### 2 使用对象关系映射器描述数据模型

- Django默认使用Python自带的SQLite。
- 可以不通过表和SQL语句，就在Django中实现数据库的创建、增删改查。

#### 2.1 数据库配置

打开 `mysite/settings.py` 。先设置 [`TIME_ZONE`](https://docs.djangoproject.com/zh-hans/3.0/ref/settings/#std:setting-TIME_ZONE) 为你自己时区（`'Asian/Shanghai'`）。

- 文件头部的 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/3.0/ref/settings/#std:setting-INSTALLED_APPS)  设置项，这里包括了会在你项目中启用的所有 Django 应用。

使用这些应用之前需要创建一些表。这个 [`migrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-migrate)  命令检查 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/3.0/ref/settings/#std:setting-INSTALLED_APPS) 设置，为其中的每个应用创建需要的数据表。

```
python manage.py migrate
```

#### 2.2 定义数据模型

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

- 关系表：`django.db.models.Model`的子类。数据库的表名是由应用名(`polls`)和模型名的小写形式( `question` 和  `choice`)连接而来。
- 元组：类的一个实例
- 字段：类的一个成员
- 外键：`models.ForeignKey`，默认的，Django 会在外键字段名后追加字符串 `"_id"` 。
- 主键(IDs)会被自动创建。(当然，你也可以自定义。)

#### 2.3 安装polls应用并更新数据模型

将polls应用安装在项目中：在`INSTALLED_APP`列表中添加`'polls.apps.PollsConfig'`，然后

```
python manage.py makemigrations polls
```

- `makemigrations` 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 *迁移*。

现在，再次运行 [`migrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-migrate) 命令，在数据库里创建新定义的模型的数据表

```
python manage.py migrate
```

这个 [`migrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-migrate) 命令选中所有还没有执行过的迁移并应用在数据库上 - 也就是将你对模型的更改同步到数据库结构上。

#### 2.4 动态生成的数据库API

文档：https://docs.djangoproject.com/zh-hans/3.0/topics/db/queries/

```python
Question.objects.all()  # Question表的全部元组（返回QuerySet）
q = Question(question_text="What's new?", pub_date=timezone.now()) # 新建元组
q.save() # 保存对象到数据库中
q.id # 访问元组的字段
Question.objects.filter(id=1)  # 对元组的查询（返回QuerySet）
Question.objects.get(pub_date__year=current_year)  # 返回Question
Question.objects.get(pk=1) # pk: 主键
Question.objects.order_by('-pub_date')  # 排序
q.choice_set.all() # 由外键关系自动生成的属性
q.choice_set.count()
Choice.objects.filter(question__pub_date__year=current_year)  # 两个下划线相连，可以访问相关类的属性
c.delete()
```

### 3 管理员页面

当你的模型完成定义，Django 就会自动生成一个专业的生产级 [管理接口](https://docs.djangoproject.com/zh-hans/3.0/ref/contrib/admin/)  ——一个允许认证用户添加、更改和删除对象的 Web 站点。

#### 3.1 创建管理员账号

```
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
```

#### 3.2 向管理页面中加入投票应用

告诉管理员，问题 `Question` 对象需要一个后台接口。在polls/admin.py中加入

```python
from .models import Question
admin.site.register(Question)
```

#### 3.3 进入管理站点页面

访问http://127.0.0.1:8000/admin/，登录创建的管理员用户。

- 你将会看到几种可编辑的内容：组和用户。它们是由 [`django.contrib.auth`](https://docs.djangoproject.com/zh-hans/3.0/topics/auth/#module-django.contrib.auth)  提供的，这是 Django 开发的认证框架。
- 可以对Question的字段进行管理和修改。

### 4 视图与模板

#### 4.1 从URL向视图传参

一个接受参数的视图函数（在polls/views.py中）：

```python
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

在`polls.urls`  模块里，添加 [`url()`](https://docs.djangoproject.com/zh-hans/3.0/ref/urls/#django.conf.urls.url)  函数调用

```python
# e.g.: /polls/5/vote/
urlpatterns = [
    path('<int:question_id>/vote/', views.vote, name='vote'), 
    ...]
```

- 使用尖括号“捕获”这部分 URL，且以关键字参数的形式发送给视图函数。
  - `:question_id>` 部分定义了将被用于区分匹配模式的变量名，而 `int:` 则是一个转换器决定了应该以什么变量类型匹配这部分的 URL 路径。

#### 4.2 在视图中做其他事情

- 每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 [`HttpResponse`](https://docs.djangoproject.com/zh-hans/3.0/ref/request-response/#django.http.HttpResponse) 对象，或者抛出一个异常，比如 [`Http404`](https://docs.djangoproject.com/zh-hans/3.0/topics/http/views/#django.http.Http404) 。至于你还想干些什么，随便你。
- 你的视图可以从数据库里读取记录，可以使用一个模板引擎（比如 Django 自带的，或者其他第三方的），可以生成一个 PDF 文件，可以输出一个 XML，创建一个 ZIP 文件，你可以做任何你想做的事，使用任何你想用的 Python 库。

#### 4.3 创建模板

HTML的基础：https://developer.mozilla.org/zh-CN/docs/learn/HTML/Introduction_to_HTML/Getting_started

在你的 `polls` 目录里创建一个 `templates` 目录。Django 将会在这个目录里查找模板文件。

在你刚刚创建的 `templates` 目录里，再创建一个目录 `polls`，然后在其中新建一个文件 `index.html` 。Django可以引用到 `polls/index.html`  这一模板了。

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

- 模板HTML中的语法：https://docs.djangoproject.com/zh-hans/3.0/topics/templates/#the-django-template-language
  - 变量用{{}}括起来
  - 标签Tag提供任意的逻辑，如控制结构for和if，用{% %}括起来

#### 4.4 在视图中载入模板

```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')  # 载入模板
    context = {
        'latest_question_list': latest_question_list,
    }  # 上下文是一个字典，它将模板内的变量映射为 Python 对象
    return HttpResponse(template.render(context, request))  # 向模板传递一个上下文
```

- render函数：载入模板，填充上下文，再返回由它生成的 [`HttpResponse`](https://docs.djangoproject.com/zh-hans/3.0/ref/request-response/#django.http.HttpResponse)  对象

```python
from django.shortcuts import render
render(request, 'polls/index.html', context)
```

#### 4.5 抛出404错误

```python
from django.http import Http404
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

或者使用函数 [`get_object_or_404()`](https://docs.djangoproject.com/zh-hans/3.0/topics/http/shortcuts/#django.shortcuts.get_object_or_404)

```python
question = get_object_or_404(Question, pk=question_id)
```

#### 4.6 使用POST上传表单

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```

我们设置表单的 `action` 为 `{% url 'polls:vote' question.id %}` ，并设置  `method="post"` 。

- 使用 `method="post"``（与其相对的是 ``method="get"`）是非常重要的，因为这个提交表单的行为会改变服务器端的数据。 无论何时，当你需要创建一个改变服务器端数据的表单时，请使用 ``method="post"` 。
- `forloop.counter` 指示 [`for`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-for) 标签已经循环多少次。
- 所有针对内部 URL 的 POST 表单都应该使用  [`{% csrf_token %}`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-csrf_token) 模板标签，防御跨站点请求伪造。

接受POST传来的数据：

```python
selected_choice = question.choice_set.get(pk=request.POST['choice'])
...
return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

- 处理完POST之后，代码应该返回一个 [`HttpResponseRedirect`](https://docs.djangoproject.com/zh-hans/3.0/ref/request-response/#django.http.HttpResponseRedirect)，只接收一个参数：用户将要被重定向的 URL。
- `reverse()` 函数避免了我们在视图函数中硬编码 URL。它需要我们给出我们想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数。



### 5 写更好的代码

#### 5.1 去除模板中的硬编码 URL

目前链接是硬编码的，但因为你在 `polls.urls` 的 [`url()`](https://docs.djangoproject.com/zh-hans/3.0/ref/urls/#django.conf.urls.url) 函数中通过 name 参数为 URL 定义了名字，你可以使用  `{% url %}` 标签代替它

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

#### 5.2 为 URL 名称添加命名空间

在 `polls/urls.py` 文件中稍作修改，加上 `app_name` 设置命名空间，让Django知道 `{% url %}` 标签到底对应哪一个应用的 URL。

```python
app_name = 'polls'
```

在模板中使用name的地方的前面加上polls:

```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

#### 5.3 竞争条件问题

https://docs.djangoproject.com/zh-hans/3.0/ref/models/expressions/#avoiding-race-conditions-using-f

#### 5.4 使用通用视图来解耦

- 基本的 Web 开发中的一个常见情况：根据 URL 中的参数从数据库中获取数据、载入模板文件然后返回渲染后的模板。 由于这种情况特别常见，Django 提供一种快捷方式，叫做“通用视图”系统。

首先更新URLconf

```python
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

改良视图

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
```

- 两个通用视图： [`ListView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView) 和 [`DetailView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) 。
  - 这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。

#### 5.6 测试你的代码

略

### 6 静态文件

CSS教程：https://www.w3school.com.cn/css/css_syntax.asp

https://developer.mozilla.org/zh-CN/docs/Learn/CSS/First_steps/%E5%BC%80%E5%A7%8B

- 网络应用通常需要一些额外的文件——比如图片，脚本和样式表——来帮助渲染网络页面。在 Django 中，我们把这些文件统称为“静态文件”。

#### 6.1 添加CSS样式表

首先，在你的 `polls` 目录下创建一个名为 `static` 的目录。Django 将在该目录下查找静态文件。

在你刚创建的 `static` 文件夹中创建一个名为 `polls` 的文件夹，再在 `polls` 文件夹中创建一个名为 `style.css` 的文件。你可以在 Django 中以 `polls/style.css` 的形式引用此文件。

将以下代码放入样式表

```css
li a {
    color: green;
}
```

下一步，在 `polls/templates/polls/index.html` 的文件头添加以下内容：

```html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```

- `{% static %}` 模板标签会生成静态文件的绝对路径。

#### 6.2 添加背景图

创建一个用于存在图像的目录。在 `polls/static/polls` 目录下创建一个名为 `images` 的子目录。在这个目录中，放一张名为 `background.gif` 的图片。

在样式表中添加

```css
body {
    background: white url("images/background.gif") no-repeat;
}
```

### 7 Django 模板语言

- 基于模板，生成文本文件（HTML, CSV, XML... ) 。
- 模板文件中包含的 **变量** 被替换为变量的值, **标签** 被替换为相应的模板控制逻辑。

#### 7.1 变量

- 模板文件中的变量：`{{ variable }}`。
- 当模板引擎遇到一个变量，将`{{ variable }}`替换为变量的值。
- 使用点 (`.`) 来访问变量的属性. e.g. `{{ section.title }}`

#### 7.2 过滤器

- 通过使用 **过滤器** 修改变量的显示： `{{ name|lower }}`
- 过滤器可以是 "链式的". 一个过滤器的输出作为下一个过滤器的输入.  `{{ text|escape|linebreaks }}` 
- 带参数的过滤器: `{{ bio|truncatewords:30 }}`. 
- 常用过滤器：
  - default: If a variable is false or empty, use given default
  - length: 变量的长度
  - filesizeofformat: 将数值转化为文件大小的格式

```django
{{ value|default:"nothing" }}
{{ value|length }}
{{ value|filesizeformat }}
```

- 所有过滤器：https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#ref-templates-builtins-filters

#### 7.3 标签

- 标签看起来像这样: `{% tag %}`.
  - 有些标签在使用时需要有开始和结束标签 (像这样 `{% tag %} ... 内容 ... {% endtag %}`)
- 有些标签会创建一段文本, 有些标签会控制输出流的方式比如循环或逻辑条件, 还有些标签会添加一些扩展内容到模板中, 比如另外的标签和过滤器.
- 常见标签：
  - for: 循环数组中的每个元素
  - if, elif, else: 判断一个变量的布尔值, 如果它为 "true" 则显示 `if` 块儿内的内容, 否则显示 `else` 块儿内的文字
    - 也可以在 [`if`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-if) 标签里使用过滤器和各种操作符
  - block, extends: 用于模板继承

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

```django
{% if athlete_list|length > 1 %}
   Team: {% for athlete in athlete_list %} ... {% endfor %}
{% else %}
   Athlete: {{ athlete_list.0.name }}
{% endif %}
```

- 所有标签参考：https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#ref-templates-builtins-tags

#### 7.4 注释

- 单行注释： `{# #}`
- 多行注释：ignores everything between `{% comment %}` and `{% endcomment %}`. 
  - An optional note may be inserted in the first tag. 

```django
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
```

#### 7.5 模板继承

- 在父模板中，使用 [`block`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-block) 标签定义可以被子模板填充的块. [`block`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-block) 标签告诉了模板系统哪些地方可能被子模板覆盖.

base.html:

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

- 在子模板中，使用[`extends`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-extends) 标签告诉模板系统这个模板继承了另外的模板
  - 必须位于模板的最开始. 如果在其他的部分声明, 则不生效.
- 模板引擎会在 `base.html` 中发现三个 [`block`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-block) 标签, 并且使用子模板的内容替换掉这些块.

```django
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```

- 如果父模板有块没有在子模板中被定义，那么父模板的内容就会被使用
- 如果你需要得到父模板块中的内容, 可以用 `{{ block.super }}` 变量.

- 模板继承的常用方案：三层继承.
  - 创建一个 `base.html` 模板把控你网站的整体风格.
  - 为网站的每个子分类创建一个 `base_SECTIONNAME.html` 模板. 比如, `base_news.html`, `base_sports.html`. 这些模板都继承 `base.html` 模板. 这些模板中包含特定的设计/风格.
  - 为每一种类型的页面创建一个模板, 比如 `news` `article` 或 `blog` 内容. 这些模板扩展上一级模板的相应分类.