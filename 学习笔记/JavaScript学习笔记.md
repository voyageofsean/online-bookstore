# JavaScript学习笔记

- JavaScript 是标准 Web 技术蛋糕的第三层。
- [JavaScript](https://developer.mozilla.org/zh-CN/docs/Glossary/JavaScript) 是一种脚本语言，可以用来创建动态更新的内容，控制多媒体，制作图像动画，还有很多。
- JavaScript 是轻量级解释型语言。浏览器接受到JavaScript代码，并以代码自身的文本格式运行它。
- JavaScript 也可用作服务器端语言，比如现在流行的 Node.js 环境。



## 1 基本JavaScript

### 1.1 运行次序

- HTML 元素是按其在页面中出现的次序调用的，如果用 JavaScript 来管理页面上的元素（更精确的说法是使用 [文档对象模型](https://developer.mozilla.org/zh-CN/docs/Web/API/Document_Object_Model) DOM），若 JavaScript 加载于欲操作的 HTML 元素之前，则代码将出错。

- 当浏览器执行到一段 JavaScript 代码时，通常会按从上往下的顺序执行这段代码。
  - 这里我们选定一个文本段落，然后给它附上一个事件监听器，使得在它被点击时，`updateName()`便会运行。
  - `updateName()` 向用户请求一个新名字，然后把这个名字插入到段落中以更新显示。

```js
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  let name = prompt('输入一个新的名字：');
  para.textContent = '玩家1：' + name;
}
```

- 为防止脚本调用时，所操作的HTML元素尚未加载，解决办法：
  - 使用事件监听器，它监听浏览器的 "`DOMContentLoaded`" 事件，即 HTML 文档体加载、解释完毕事件。

```js
document.addEventListener("DOMContentLoaded", function() {
  . . .
});
```

- 使用`<script>`元素的`async` “异步”属性告知浏览器在遇到 `<script>` 元素时不要中断后续 HTML 内容的加载。
  - 如果有多个脚本，且后面的脚本依赖于前面的脚本，那么应该使用`<script>`元素的 `defer`属性，将关联的脚本按所需顺序置于 HTML 中。
- 旧方法是：把脚本元素放在文档体的底端（`</body>` 标签之前，与之相邻）

### 1.2 在页面中添加JS

#### 1.2.1  内部 JavaScript  

```html
<script>
  // JS代码
</script>
```

#### 1.2.2 外部 JavaScript

```html
<script src="script.js" async></script>
```

#### 1.2.3 内联 JavaScript 处理器

- 不推荐使用

```js
<button onclick="createParagraph()">点我呀</button>
```

### 1.3 语句

- 分号用于分隔 JavaScript 语句。
- 注释：在双斜杠后添加单行注释；在 `/*` 和 `*/` 之间添加多行注释

- JavaScript 会忽略多余的空格
- 可以在文本字符串中使用反斜杠对代码行进行换行。



## 2 JavaScript程序设计

### 2.1 声明变量和常量

```js
//得出一个 1 到 100 之间的随机数，并赋值给第一个变量
let randomNumber = Math.floor(Math.random() * 100) + 1; 
//三个常量均存储着一个引用，分别指向HTML结果段落中某个元素，用于在代码后面段落中插入值
const guesses = document.querySelector('.guesses'); 
const lastResult = document.querySelector('.lastResult');
const lowOrHi = document.querySelector('.lowOrHi');
//两个常量存储对表单文本输入和提交按钮的引用，并用于控制以后提交猜测
const guessSubmit = document.querySelector('.guessSubmit');
const guessField = document.querySelector('.guessField');
//存储一个计数器并初始化为 1（用于跟踪玩家猜测的次数），最后一个变量存储对重置按钮的引用
let guessCount = 1;
let resetButton;
```

- let, const, var
- document.querySelector()

### 2.2 函数

```js
function myFunction(a, b) {
    return a * b;
} 
```

### 2.3 操作符

- `+ - * /`, `+=`, `++ --`, `**`幂，`%`求余
  - +也可以用来串联字符串

- `==` 等于 `!=` 不等于，`> < <= >=` 
- `===`绝对等于（值和类型均相等）  `!==`  不绝对等于（值和类型有一个不相等，或两个都不相等）
- `&& || !` 
- `condition?val1:val2`

### 2.4 控制流

- 条件语句

```js
if (userGuess === randomNumber) {
  } else if (guessCount === 10) {
  } else {
  }

switch (expression) {
  case choice1:
    //run this code
    break;

  case choice2:
    //run this code instead
    break;

  default:
    //actually, just run this code
}
```

- 循环

```js
for (let i = 0 ; i < resetParas.length ; i++) {
  resetParas[i].textContent = '';
}

while (exit-condition) {
  // code to run
}

do {
  // code to run

  final-expression
} while (exit-condition)
```

### 2.5 数据类型

```js
var length = 16;                                  // Number 通过数字字面量赋值
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值
var x=true;
```

- 动态类型

```js
let myNumber = '500'; // oops, this is still a string
typeof myNumber;
myNumber = 500; // much better — now this is a number
typeof myNumber
```

### 2.6 对象

- JavaScript 中一切都是对象。

```js
const guessField = document.querySelector('.guessField');
guessField.focus();
guessField.value = 'Hello';
guesses.style.backgroundColor = 'yellow';
```

- 页面上的每个元素都有一个 `style` 属性，它本身包含一个对象，其属性包含应用于该元素的所有内联 CSS 样式。

### 2.7 数组

```js
let random = ['tree', 795, [0, 1, 2]];
random[0] = 'tahiti'
random[2][2];
random.length
```

- 添加删除数组项

```js
myArray.push('Cardiff'); // push返回新数组长度
myArray.push('Bradford', 'Brighton');
myArray.pop(); //pop返回删除的项目

myArray.unshift('Edinburgh'); //在左侧插入
let removedItem = myArray.shift(); //删除第一个
```

### 2.8 字符串

- 单双引号都可以
- 转义字符
- 字符串+数字得到字符串，Number(str)，num.toString()

```js
str.length;
str[0]; str.slice(0,3); str.slice(2); //（从2之后）
str.indexOf(substr);
str.toLowerCase(); str.toUpperCase();
str = str.replace(substr, sth);
```

- 字符串和数组的转换

```js
let myData = 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle';
let myArray = myData.split(',');
let muArray = myData.toString();
let myNewString = myArray.join(',');
```



## 3 JavaScript 对象

### 3.1 创建对象

```js
var person = {};

var person = {
  name : ['Bob', 'Smith'],
  age : 32,
  gender : 'male',
  interests : ['music', 'skiing'],
  bio : function() {
    alert(this.name[0] + ' ' + this.name[1] + ' is ' + this.age + ' years old. He likes ' + this.interests[0] + ' and ' + this.interests[1] + '.');
  },
  greeting: function() {
    alert('Hi! I\'m ' + this.name[0] + '.');
  }
};
```

- 关键字"this"指向了当前代码运行时的对象

- 点表示法：`person.age`
- 括号表示法：`person['age']`

### 3.2 类

定义类的构造函数

```js
function Person(name) {
  this.name = name;
  this.greeting = function() {
    alert('Hi! I\'m ' + this.name + '.');
  };
}
```

用构造函数创建实例

```js
var person1 = new Person('Bob');
```

### 3.3 对象原型和继承

略



## 4 函数

### 4.1 自定义函数

```js
function random(number) {
  return Math.floor(Math.random()*number);
}
```

### 4.2 匿名函数

```js
myButton.onclick = function() {
  alert('hello');
}
var myGreeting = function() {
  alert('hello');
}
myGreeting();
```

### 4.3 函数作用域

- 所有函数的最外层被称为全局作用域。
- 当你创建一个函数时，函数内定义的变量和其他东西都在它们自己的单独的范围内



## 5. 事件

### 5.1 事件

- 事件是您在编程时系统内发生的动作或者发生的事情，系统响应事件后，如果需要，您可以某种方式对事件做出回应。

- 每个可用的事件都会有一个**事件处理器**，也就是事件触发时会运行的代码块。
- 事件列表：https://developer.mozilla.org/en-US/docs/Web/Events
- 事件对象：被自动传递给事件处理函数，以提供额外的功能和信息，例如`event`，`evt`或简单的`e`
  - 事件对象 `e` 的`target`属性始终是事件刚刚发生的元素的引用。
  - `e.preventDefault();`阻止默认行为

### 5.2 事件处理器

```js
var btn = document.querySelector('button');
btn.onclick = function() {
  var rndCol = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')';
  document.body.style.backgroundColor = rndCol;
}
```

-  `onclick` 是被用在这个情景下的事件处理器的属性
  - 当您将一个函数赋值给它的时候，只要事件触发代码就会运行。

### 5.3 新的事件触发机制

```js
var btn = document.querySelector('button');

function someFunc() {
  // do sth
}   

btn.addEventListener('click', someFunc);
```

- 相对应有一个移除事件监听器的方法：

```js
btn.removeEventListener('click', someFunc);
```

- 下列情况两个函数都会工作：

```js
myElement.addEventListener('click', functionA);
myElement.addEventListener('click', functionB);
```

### 5.4 事件冒泡

当一个事件发生在具有父元素的元素上：冒泡

- 浏览器检查实际点击的元素是否在冒泡阶段中注册了一个`onclick`事件处理程序，如果是，则运行它
- 然后它移动到下一个直接的祖先元素，并做同样的事情，然后是下一个，等等，直到它到达`<html>`元素。

在现代浏览器中，默认情况下，所有事件处理程序都在冒泡阶段进行注册。

用`e.stopPropagation();`阻止冒泡链的传播。