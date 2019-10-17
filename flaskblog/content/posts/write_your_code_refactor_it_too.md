title: Write Your Code, and Refactor it Too!
author: Jeff Yang
published: 2019-04-28
category: Internship
summary: My first SWE internship, I'd like to think I definitely learned a lot from this one.

Summer 2017 Knowru SWE Internship

After hours of debugging, BOOM. Your code finally runs. We all know how that feels – it’s the very reason why we all enjoy coding. The more experienced developers know how to calm down, and get back to work; they understand that writing functional code isn’t the end of the process. On the other hand, the less experienced programmers tend to shake their hands off right away and type “git push origin master” on their command line. It’s a fully-functional and working code that they just pushed to their git repository, so what could possibly be wrong? Well, the last step – the refactoring process still awaits.

What does it mean to refactor code? According to Wikipedia, code refactoring is the process of restructuring existing computer code – changing the factoring – without changing its external behavior. In other words, refactoring has to do with improving the readability of your code so that it’s easier for other developers to understand your code, and to enhance the maintainability of your code in general.

Let us take a look at some simple code to better illustrate the importance of refactoring.

Here is a code snippet (javascript/jquery) before refactoring:

```javascript
function reloadTable(elementToRefresh) {
    var refreshElement = "#" + elementToRefresh;
    $(refreshElement).load(" #dataTable", function fontColorChange() {
	$('.knowrucom').each(function() {
          $(this).css('color', 'red');
	}	
	)});      
}

function tableAutoReload() {
    $(document).ready(function() {
        setInterval(function autoReload() {
            reloadTable('tableDiv');
        }, 30000)
    });
}
```


The `reloadTable()` function above is a simple javascript function written using the jquery library that changes the font color of selected elements. This function is then utilized by the `tableAutoReload()` function that calls `reloadTable()` every 5 minutes. This code does the job of changing the font color for some elements, but is the code maintainable? Is the code easily readable? If a future developer wants to use the same `reloadTable()` function to change the font size, is the job for him/her going to be easy and smooth?

Now, let us take a look at a refactored version:

```javascript
function fontColorChange() {
    $('.knowrucom').each(function() {
    $(this).css('color', 'red');
});
}

function backgroundColorChange() {
    $('.helloknowru').each(function() {
    $(this).css('background-color', 'blue');
});
}

function autoReloadCallBack() {
    fontColorChange();
    backgroundColorChange();
}

function reloadTable(elementToRefresh) {
    var refreshElement = '#' + elementToRefresh;
    $(refreshElement).load('#dataTable', autoreloadCallBack);
}  

function tableAutoReload() {
    $(document).ready(function() {
        setInterval(function autoReload() {
            reloadTable('tableDiv');
        }, 30000)
    })
}
```

This code may seem longer, but it is now much more organized. Instead of writing a callback function entirely inside the `reloadTable()` function, there is now a separate `autoReloadCallBack()` function which can call however many other functions. The functions inside `autoReloadCallBack()` function is defined outside. After refactoring, it’s easier to read code, and to maintain code. If there is an unexpected error some couple of weeks later, it will be much easier to debug since the functions are separated. If a new junior developer wants to call any other function as a callback, he/she can simply write a function and call that function inside `autoReloadCallBack()`. Now everything’s easier, right?

Decide for yourself; would you like to work with a partner who writes sin(π/6)*[√4] + (3!)^2 – (46,656)^(1/3) instead of just “1”? Simplicity generally isn’t a negative concept, but in programming, it certainly is something that all programmers should strive for.