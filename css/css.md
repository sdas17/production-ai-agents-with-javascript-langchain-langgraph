<!-- CSS Quick Notes
<link>
Use: Connect external CSS file.
<link rel="stylesheet" href="style.css">
rel
Use: Defines the relationship.
stylesheet → CSS file.
<link rel="stylesheet" href="style.css">
href
Use: Specifies the file/URL path.
<a href="https://google.com">Google</a>
src
Use: Specifies the source of images, JS, videos.
<img src="logo.png">
<script src="app.js"></script>
Box Model
Margin
Outside the element.
Use: Space between elements.
margin:20px;
Padding
Inside the element.
Use: Space between content and border.
padding:20px;
Width
Use: Set element width.
width:300px;
Height
Use: Set element height.
height:200px;
<div>
Use: Groups HTML elements and creates layouts.
<div>Content</div>
Font
font-family
Use: Change font style.
font-family: Arial, sans-serif;
font-size
Use: Change text size.
font-size:24px;
font-weight
Use: Make text bold/light.
font-weight:bold;
Border
Border
Use: Add border around an element.
border:1px solid black;
Border Radius
Use: Make rounded corners.
border-radius:10px;
CSS Specificity (Priority)
Inline Style ⭐⭐⭐⭐
ID (#id) ⭐⭐⭐
Class (.class) ⭐⭐
Element (div, p) ⭐

Example:

#title { color:red; }
.heading { color:blue; }
p { color:green; }
CSS Selectors
a, b
Use: Select multiple elements.
h1, p { color:red; }
a b
Use: Select all descendants.
div p { color:blue; }
a > b
Use: Select direct child only.
div > p { color:red; }
a + b
Use: Select immediate next sibling.
h1 + p { color:green; }
[a=b]
Use: Select by attribute.
input[type="text"]{
    border:1px solid blue;
}
a:b
Pseudo-class
Use: Style element in a state.
button:hover{
    background:black;
}
a::b
Pseudo-element
Use: Style part of an element.
p::first-letter{
    font-size:30px;
}
⭐ Interview Tip

Margin → Outside the box
Padding → Inside the box

Inline > ID > Class > Element (Specificity order) -->



<!-- responsive design
view port
flex
media query
grid 
content ="width=device-width,inital-scale=1.0
<meta name='viewport' >


flex box 








 -->