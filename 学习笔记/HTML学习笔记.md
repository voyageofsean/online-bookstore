

HTML学习笔记

## 1. HTML基本概念

- [HTML](https://developer.mozilla.org/zh-CN/docs/Glossary/HTML) (HyperText Markup Language) 不是一门编程语言，而是一种用来告知浏览器如何组织页面的**标记语言**。

### 1.1 标签和元素

- 一对**标签**（[tags](https://developer.mozilla.org/zh-CN/docs/Glossary/Tag)）可以为一段文字或者一张图片添加超链接，将文字设置为斜体，改变字号，等等。
  - HTML 标签是由*尖括号*包围的关键词，比如` <html>`
  - HTML 标签通常是*成对出现*的，比如 `<b>` 和`</b>`
- HTML文件由一系列的**元素**（[elements](https://developer.mozilla.org/zh-CN/docs/Glossary/元素)）组成。

![img](https://mdn.mozillademos.org/files/16475/element.png)

- 元素之间可以嵌套，但不能交叉。
- 块级元素和内联元素
  - 块级元素在页面中以块的形式展现 —— 相对于其前面的内容它会出现在新的一行，其后的内容也会被挤到下一行展现。
    - e.g. 段落`<p></p>`
  - 内联元素通常出现在块级元素中，包围一小部分，不会导致文本换行。
    - e.g. 强调`<em></em>` 强调`<strong></strong>`
- 空元素：一些元素只有一个标签，通常用来在此元素所在位置插入/嵌入一些东西。
  - e.g. 插入图片`<img src="http://url">`

### 1.2 属性

- 元素也可以拥有属性，属性包含元素的额外信息，这些信息不会出现在实际的内容中。

![&amp;amp;amp;lt;p class="editor-note">我的猫咪脾气爆&amp;amp;amp;lt;/p>](https://mdn.mozillademos.org/files/16476/attribute.png)

- 两个元素的属性
  - `<p>`的class属性给元素赋了一个识别的名字（id），这个名字此后可以被用来识别此元素的样式信息和其他信息。
  - `<a>`元素使被标签包裹的内容成为一个超链接，其属性：
    - `href`: 这个属性声明超链接的web地址，e.g. `href="https://www.mozilla.org/"`
    - `title`: 标题`title`属性，例如：`title="The Mozilla homepage"`。
    - `target`: 目标`target`属性用于指定链接如何呈现出来。例如，`target="_blank"`将在新标签页中显示链接。
- 布尔属性：只能有跟它的属性名一样的属性值，因此可省略=后面的

```html
<input type="text" disabled="disabled">
<input type="text" disabled>
```

### 1.3 HTML文档的构成

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>我的测试站点</title>
  </head>
  <body>
    <p>这是我的页面</p>
  </body>
</html>
```

- `<!DOCTYPE html>`: 声明文档类型
- `<html></html>`: `<html>`元素。这个元素包裹了整个完整的页面，是一个根元素。
- `<head></head>`这个元素是一个容器，它包含网页元数据，如CSS样式，字符集声明等。

  - `<meta charset="utf-8">`: 这个元素设置文档使用utf-8字符集编码
  - `<title></title>`: 设置页面标题
- `<body></body>`: `<body>`元素。 包含了你访问页面时所有显示在页面上的内容，文本，图片，音频，游戏等等。

### 1.4 HTML语言特性

#### 1.4.1  空白符

- 无论你在HTML元素的内容中使用多少空格(包括空白字符，包括换行)，当渲染这些代码的时候，HTML解释器会将连续出现的空白字符减少为一个单独的空格符。

#### 1.4.2 实体引用

- 在HTML中，字符 `<`, `>`,`"`,`'` 和 `&` 是特殊字符。
- 字符引用 —— 表示字符的特殊编码, 它们可以在那些情况下使用。每个字符引用以符号&开始, 以分号(;)结束。

| 原义字符 | 等价字符引用 |
| :------- | :----------- |
| <        | `&lt;`         |
| >        | `&gt;`         |
| "        | `&quot;`       |
| '        | `&apos;`       |
| &        | `&amp;`        |

#### 1.4.3 注释

用特殊的记号`<!--`和`-->`包括起来

```html
<!-- <p>我在注释内！</p> -->
```



## 2. HTML头部

- HTML 头部是包含在`<head>`元素里面的内容。不像`<body>`元素的内容会显示在浏览器中，head 里面的内容不会在浏览器中显示，它的作用是包含一些页面的[元数据](https://developer.mozilla.org/zh-CN/docs/Glossary/Metadata)。

### 2.1 标题和网页图标

- 元素`<title>`是用来表示整个HTML文档标题的元数据
  - 不要和将它和给 body 添加标题的`<h1>`元素混淆
- 网页图标
  - 将图标文件保存在与网站的索引页面相同的目录中，以.ico格式保存
  - 将以下行添加到HTML `<head>`中以引用它：

```html
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
```

### 2.2 元数据：`<meta>`元素

- HTML有一个“官方的”方式来为一个文档添加元数据—— [`<meta>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meta) 元素。
- 指定字符编码

```html
<meta charset="utf-8">
```

- 添加作者和描述
  - `name` 指定了meta 元素的类型； 说明该元素包含了什么类型的信息。
  - `content` 指定了实际的元数据内容。
  - author和description元素会在搜索引擎中被检索。

```html
<meta name="author" content="Chris Mills">
<meta name="description" content="The MDN Learning Area aims to provide
complete beginners to the Web with all they need to know to get
started with developing web sites and applications.">
```

- 有更多类型的`<meta>`元数据。
  - 许多功能都是专有的，旨在向某些网站(如社交网站)提供可使用的特定信息。
    - 例如，Facebook 编写的元数据协议 [Open Graph Data](http://ogp.me/) .

### 2.3 应用CSS和JavaScript

- 使用 [CSS](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS) 让网页更加炫酷，使用[JavaScript](https://developer.mozilla.org/zh-CN/docs/Glossary/JavaScript)让网页有交互功能。它们分别使用 [`<link>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link)元素以及 [`<script>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script) 元素。

- `<link>`元素经常位于文档的头部。rel="stylesheet"表明这是文档的样式表，而 href包含了样式表文件的路径：

```html
  <link rel="stylesheet" href="my-css-file.css">
```

- `<script>` 部分没必要非要放在文档头部；实际上，把它放在文档的尾部（在 `</body>`标签之前）是一个更好的选择

```html
<script src="my-js-file.js"></script>
```

### 2.4 语言

- 在`<html>`设置主语言

```html
<html lang="en-US">
```

- 可以将文档的分段设置为不同的语言。

```html
<p>Japanese example: <span lang="jp">ご飯が熱い。</span>.</p>
```



## 3 HTML文字部分

HTML的主要工作是编辑文本结构和文本内容（也称为语义[semantics](https://developer.mozilla.org/zh-CN/docs/Glossary/语义)），以便浏览器能正确的显示。 

### 3.1 标题和段落

- 段落：

```html
<p>我是一个段落，千真万确。</p>
```

- 标题：有六级标题元素标签 —— `<h1>`、`<h2>`、`<h3>`、`<h4>`、`<h5>`、`<h6>`。

```html
<h1>我是文章的标题</h1>
```

### 3.2 列表

- 列表可以嵌套。

- 无序列表

```html
<ul>
  <li>豆汁</li>
  <li>焦圈</li>
</ul>
```

- 有序列表（1. 2. ...）

```html
<ol>
  <li>沿着条路走到头</li>
  <li>右转</li>
  <li>直行穿过第一个十字路口</li>
  <li>在第三个十字路口处左转</li>
  <li>继续走 300 米，学校就在你的右手边</li>
</ol>
```

- 描述列表

```html
<dl>
  <dt>内心独白</dt>
    <dd>戏剧中，某个角色对自己的内心活动或感受进行念白表演，这些台词只面向观众，而其他角色不会听到。</dd>
  <dt>语言独白</dt>
    <dd>戏剧中，某个角色把自己的想法直接进行念白表演，观众和其他角色都可以听到。</dd>
  <dt>旁白</dt>
    <dd>戏剧中，为渲染幽默或戏剧性效果而进行的场景之外的补充注释念白，只面向观众，内容一般都是角色的感受、想法、以及一些背景信息等。</dd>
    <dd>写作中，指与当前主题相关的一段内容，通常不适于直接置于内容主线中，因此置于附近的其它位置（通常位于主线内容旁边一个文本框内）。</dd>
</dl>
```

### 3.3 强调

- 用[`<em></em>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/em)（emphasis）元素来标记强调，默认显示为斜体。
- 用[`<strong></strong>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/strong) (strong importance) 元素来标记非常重要，默认显示为粗体。
- 注意：上述都是有语义的，如果想要仅仅外观上的斜体/粗体，不应使用它们。应使用**表象元素（presentational elements）**。
  - 使用`<b>`,`<i>`,`<u>` 来传达传统意义上的粗体，斜体或下划线。

### 3.4 引用

- 如果一个块级内容（一个段落、多个段落、一个列表等）从其他地方被引用，你应该把它用[`<blockquote>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/blockquote)元素包裹起来表示，并且在`cite`属性里用URL来指向引用的资源。

```html
<blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
  <p>Something quoted.</p>
</blockquote>
```

- 行间引用，使用`<q></q>`元素。

- 使用`<cite>`元素可以表示引文的来源。

### 3.5 其他

- 缩略语`<abbr>`

- 联系方式`<address>`

- 上下标`<sup>``<sub>`

- 代码`<code>` `<pre>` `<samp>`

- 时间日期`<time>`

```html
  <time datetime="2016-01-20">2016年1月20日</time>
```

### 3.6 表格

参见：https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Tables

- 表格由 `<table>` 标签来定义。
  - 表格的表头使用 `<th>` 标签进行定义。
  - 每个表格均有若干行（由 `<tr>` 标签定义），每行被分割为若干单元格（由 `<td> `标签定义）
  - border属性：是否有边框

```html
<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```

### 3.7 表单

- 参见：https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Forms

- 表单元素是允许用户在表单中输入内容，比如：文本域(textarea)、下拉列表、单选框(radio-buttons)、复选框(checkboxes)等等。
- 表单使用标签`<form></form>`来设置

```html
<form>
User name: <input type="text" name="username"><br>
Password: <input type="password" name="pwd"><br>
</form>
```

- 单选按钮

```html
<form>
<input type="radio" name="sex" value="male">Male<br>
<input type="radio" name="sex" value="female">Female
</form>
```

- 复选框

```html
<form>
<input type="checkbox" name="vehicle" value="Bike">I have a bike<br>
<input type="checkbox" name="vehicle" value="Car">I have a car
</form>
```

- 提交按钮

```html
<form name="input" action="html_form_action.php" method="get">
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>
```

- 下拉菜单 略

  

## 4. 超链接

### 4.1 将内容变成超链接

- 通过将文本（或其他内容，见[块级链接](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks#块级链接))转换为[`<a>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a)元素内的链接来创建基本链接， 给它一个`href`属性（也称为目标），它将包含您希望链接指向的网址。使用title属性添加支持信息。

```html
<p>I'm creating a link to
<a href="https://www.mozilla.org/en-US/"
   title="The best place to find more information about Mozilla's
          mission and how to contribute">the Mozilla homepage</a>.
</p>
```

- 块状元素也可以变成超链接。

```html
<a href="https://www.mozilla.org/en-US/">
  <img src="mozilla-image.png" alt="mozilla logo that links to the mozilla homepage">
</a>
```

### 4.2 链接到文档内部

- 首先给要链接到的元素分配一个`id`属性。

```html
<h2 id="Mailing_address">Mailing address</h2>
```

- 然后链接到那个特定的`id`，您可以在URL的结尾使用一个井号指向它。

```html
<p>Want to write us a letter? Use our <a href="contacts.html#Mailing_address">mailing address</a>.</p>
<p>The <a href="#Mailing_address">company mailing address</a> can be found at the bottom of this page.</p>
```



## 5. 网页布局

### 5.1 网页的布局

- `<header>`：页眉。
- `<nav>`：导航栏。
- `<main>`：主内容。主内容中还可以有各种子内容区段，可用`<article>`、`<section>` 和 `<div>` 等元素表示。
  - 每个页面上只能用一次 `<main>`，且直接位于 [`<body>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/body) 中。最好不要把它嵌套进其它元素。
  - [`<article>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/article) 包围的内容即一篇文章，与页面其它部分无关（比如一篇博文）。
  - [`<section>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/section) 与 `<article>` 类似，但 `<section>` 更适用于组织页面使其按功能（比如迷你地图、一组文章标题和摘要）分块。
- `<aside>`：侧边栏，经常嵌套在 `<main>` 中。
  - 如果它是`<body>`的子元素，那么就是网站的全局页眉。
  - 如果它是`<article>`或`<section>`的子元素，那么它是这些部分特有的页眉。
- `<footer>`：页脚。

###  5.2 布局元素细节

#### 5.2.1 无语义元素

- 有时候你可能只想将一组元素作为一个单独的实体来修饰来响应单一的用 [CSS](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS) 或 [JavaScript](https://developer.mozilla.org/zh-CN/docs/Glossary/JavaScript)。为了应对这种情况，HTML提供了 [`<div>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/div) 和 [`<span>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/span) 元素。
- 应配合使用 `class` 属性提供一些标签，使这些元素能易于查询。
- [`<span>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/span) 是一个内联的（inline）无语义元素

```html
<p>国王喝得酩酊大醉，踉跄地走过门口。<span class="editor-note">[编辑批注：此刻舞台灯光应变暗]</span>.</p>
```

- `<div>` 是一个块级无语义元素

#### 5.2.2 换行和分割线

- `<br>` 可在段落中进行换行；

```html
<p>他说写 HTML 感觉最好<br>
但他写的代码结构语义一团糟<br>
他写的标签谁也懂不了。</p>
```

- `<hr>` 元素在文档中生成一条水平分割线



## 6 多媒体

### 6.1 图片

```html
<img src="images/dinosaur.jpg">
```

更多属性：https://www.runoob.com/html/html-images.html

### 6.2 视频和音频

```html
<video src="rabbit320.webm" controls>
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="rabbit320.mp4">此链接</a>观看</p>
</video>
```

按照兼容性自动换源：

```html
<video controls>
  <source src="rabbit320.mp4" type="video/mp4">
  <source src="rabbit320.webm" type="video/webm">
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="rabbit320.mp4">此链接</a>观看</p>
</video>
```

```html
<audio controls>
  <source src="viper.mp3" type="audio/mp3">
  <source src="viper.ogg" type="audio/ogg">
  <p>你的浏览器不支持 HTML5 音频，可点击<a href="viper.mp3">此链接</a>收听。</p>
</audio>
```

更多：https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content

### 6.3 iframe嵌入

- `<iframe>`元素旨在允许您将其他Web文档嵌入到当前文档中。这很适合将第三方内容纳入您的网站。

```html
<iframe src="https://player.bilibili.com/player.html?aid=19390801&cid=31621681&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
```

[更多关于嵌入](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Multimedia_and_embedding/其他嵌入技术)

### 6.4 矢量图形

插入svg图像就用`<img>`，也可以手动绘制：

```html
<svg width="300" height="200">
    <rect width="100%" height="100%" fill="green" />
</svg>
```