# CSS学习笔记

## 1 CSS基本语法

- CSS是一门基于规则的语言 —— 你能定义用于你的网页中特定元素样式的一组规则.

![img](https://mdn.mozillademos.org/files/11781/rendering.svg)

### 1.1 CSS基本规则

- 语法由一个 [选择器(selector)](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS_Selector)起头。 它 *选择(selects)* 了我们将要用来添加样式的 HTML 元素。

- 接着输入一对大括号`{ }`。 在大括号内部定义一个或多个形式为 **属性(property):值(value);** 的 **声明(declarations)**
  - 不同的 CSS [属性(properties)](https://developer.mozilla.org/en-US/docs/Glossary/property/CSS) 对应不同的合法值。

```css
h1 {
    color: red;
    font-size: 5em;
}
```

- 一个 CSS 样式表可以包含很多个规则。
- 可一次使用多个选择器。

```css
p, li {
    color: green;
}
```

### 1.2 根据类确定样式

- 例如，把 [class 属性](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class)加到表里面第二个对象。

```html
<ul>
  <li>项目一</li>
  <li class="special">项目二</li>
</ul>
```

- 要选中 `special` 类，只需在选择器的开头加个西文句点。

```css
.special {
  color: orange;
  font-weight: bold;
}
```

- 或者指定具体元素的special类

```css
li.special,
span.special {
  color: orange;
  font-weight: bold;
}
```

### 1.3 根据元素位置确定样式

- **包含选择符**：在两个选择器之间加上一个空格。
  - 下面该选择器将选择`<li>`内部的任何`<em>`元素。

```css
li em {
  color: rebeccapurple;
}
```

- **相邻选择符**：设置直接出现在一种元素后面并且与它具有相同层级的元素样式

```css
h1 + p {
  font-size: 200%;
}
```

### 1.4 根据状态确定样式

- 取决于是否是未访问的、访问过的、被鼠标悬停的、被键盘定位的，亦或是正在被点击当中的状态，这个标签有着不同的状态。
- 可以使用CSS去定位或者说针对这些不同的状态进行修饰。

```css
a:link {
  color: pink;
}
a:visited {
  color: green;
}
a:hover {
  text-decoration: none;
}
```



## 2 CSS的结构

### 2.1 在HTML中使用CSS

- 使用外部样式表：在HTML文档中，`<head>`语句模块里面加上下面的代码：

```html
<link rel="stylesheet" href="styles.css">
```

- 使用内部样式表：将CSS放在HTML文件`<head>`标签里的`<style>`标签之中。
- 内联样式：内联样式表存在于HTML元素的style属性之中。其特点是每个CSS表只影响一个元素。

```html
<h1 style="color: blue;background-color: yellow;border: 1px solid black;">Hello World!</h1>
```

### 2.2 样式冲突的规则

- 级联规则：样式表中稍后的样式将覆盖以前的样式。
- 优先级规则：类选择器比元素选择器优先级更高。
  - 具体规则参见：https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance
  - `!important`可以用来覆盖所有优先级计算，不过需要很小心的使用。

```css
.better {
    background-color: gray;
    border: none !important;
}
```

- 继承规则：一些设置在父元素上的css属性是可以被子元素继承的。
  - e.g. 如果你设置一个元素的 `color` 和 `font-family` ，每个在里面的元素也都会有相同的属性，除非你直接在元素上设置属性。



### 2.3 函数

- 虽然大多数值是相对简单的关键字或数值，但也有一些可能的值以函数的形式出现。
- calc()函数

```css
.box {
  padding: 10px;
  width: calc(90% - 30px);
  background-color: rebeccapurple;
  color: white;
}
```

- transform属性中的rotate()函数

```css
transform: rotate(0.8turn);
```

- color属性的rgb/rgba/hsl/hsla函数

### 2.4 @规则

- 导入主CSS样式表

```css
@import 'styles2.css';
```

- 媒体查询（判断某些条件是否成立）

```css
@media (min-width: 30em) {
  body {
    background-color: blue;
  }
}
```

### 2.5 速记属性

- 一些属性，如 [`font`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font), [`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background), [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding), [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border), and [`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin) 等属性称为速记属性--这是因为它们允许您在一行中设置多个属性值，从而节省时间并使代码更整洁。

```css
padding: 10px 15px 15px 5px;
background: red url(bg-graphic.png) 10px 10px repeat-x fixed;
```

### 2.6 注释

CSS中的注释以`/*`开头，以`*/`结尾。



## 3 选择器

| 选择器                                                       | 示例                | 学习CSS的教程                                                |
| :----------------------------------------------------------- | :------------------ | :----------------------------------------------------------- |
| [类型选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Type_selectors) | `h1 { }`            | [类型选择器](https://developer.mozilla.org/zh-CN/docs/user:chrisdavidmills/CSS_Learn/CSS_Selectors/Type_Class_and_ID_Selectors#Type_selectors) |
| [通配选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Universal_selectors) | `* { }`             | [通配选择器](https://developer.mozilla.org/zh-CN/docs/user:chrisdavidmills/CSS_Learn/CSS_Selectors/Type_Class_and_ID_Selectors#The_universal_selector) |
| [类选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Class_selectors) | `.box { }`          | [类选择器](https://developer.mozilla.org/zh-CN/docs/user:chrisdavidmills/CSS_Learn/CSS_Selectors/Type_Class_and_ID_Selectors#Class_selectors) |
| [ID选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/ID_selectors) | `#unique { }`       | [ID选择器](https://developer.mozilla.org/zh-CN/docs/user:chrisdavidmills/CSS_Learn/CSS_Selectors/Type_Class_and_ID_Selectors#ID_Selectors) |
| [标签属性选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Attribute_selectors) | `a[title] { }`      | [标签属性选择器](https://developer.mozilla.org/zh-CN/docs/User:chrisdavidmills/CSS_Learn/CSS_Selectors/Attribute_selectors) |
| [伪类选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Pseudo-classes) | `p:first-child { }` | [伪类](https://developer.mozilla.org/zh-CN/docs/User:chrisdavidmills/CSS_Learn/CSS_Selectors/Pseuso-classes_and_Pseudo-elements#What_is_a_pseudo-class) |
| [伪元素选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Pseudo-elements) | `p::first-line { }` | [伪元素](https://developer.mozilla.org/zh-CN/docs/User:chrisdavidmills/CSS_Learn/CSS_Selectors/Pseuso-classes_and_Pseudo-elements#What_is_a_pseudo-element) |
| [后代选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Descendant_combinator) | `article p`         | [后代运算符](https://developer.mozilla.org/zh-CN/docs/User:chrisdavidmills/CSS_Learn/CSS_Selectors/Combinators#Descendant_Selector) |
| [子代选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Child_combinator) | `article > p`       | [子代选择器](https://developer.mozilla.org/zh-CN/docs/User:chrisdavidmills/CSS_Learn/CSS_Selectors/Combinators#Child_combinator) |
| [相邻兄弟选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Adjacent_sibling_combinator) | `h1 + p`            | [相邻兄弟](https://developer.mozilla.org/zh-CN/docs/User:chrisdavidmills/CSS_Learn/CSS_Selectors/Combinators#Adjacent_sibling) |
| [通用兄弟选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/General_sibling_combinator) | `h1 ~ p`            | [通用兄弟](https://developer.mozilla.org/zh-CN/docs/User:chrisdavidmills/CSS_Learn/CSS_Selectors/Combinators#General_sibling) |