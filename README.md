**Python Tkinter - Create Button Widget**

The Tkinter Button widget is a graphical control element used in Python’s Tkinter library to create clickable buttons in a graphical user interface (GUI). It provides a way for users to trigger actions or events when clicked.

**Tkinter Button Widget Syntax**  
The syntax to use the button widget is given below.

Syntax: Button(parent, options) 


**Parameters**


*parent: This parameter is used to represents the parent window.  
*options:There are many options which are available and they can be used as key-value pairs separated by commas.

**Tkinter Button Options**  
*activebackground: Background color when the button is under the cursor.  
*activeforeground: Foreground color when the button is under the cursor.  
*anchor: Width of the border around the outside of the button.  
*bd or borderwidth: Width of the border around the outside of the button.  
*bg or background: Normal background color.  
*command: Function or method to be called when the button is clicked.  
*cursor: Selects the cursor to be shown when the mouse is over the button.  
*text: Text displayed on the button.  
*disabledforeground: Foreground color is used when the button is disabled.  
*fg or foreground: Normal foreground (text) color.  
*font: Text font to be used for the button’s label.  
*height: Height of the button in text lines.  
*highlightbackground: Color of the focus highlight when the widget does not have focus.  
*highlightcolor: The color of the focus highlight when the widget has focus.  
*highlightthickness: Thickness of the focus highlight.  
*image: Image to be displayed on the button (instead of text).  
*justify: tk.LEFT to left-justify each line; tk.CENTER to center them; or tk.RIGHT to right-justify.  
*overrelief: The relief style to be used while the mouse is on the button; default relief is tk.RAISED.  
*padx, pady: padding left and right of the text. / padding above and below the text.  
*width: Width of the button in letters (if displaying text) or pixels (if displaying an image).  
*underline: Default is -1, underline=1 would underline the second character of the button’s text.  
*width: Width of the button in letters.  
*wraplength: If this value is set to a positive number, the text lines will be wrapped to fit within this length.  

**Methods**
1. flash(): Causes the button to flash several times between active and normal colors. Leaves the button in the state it was in originally. Ignored if the button is disabled.  
2. invoke(): Calls the button’s command callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback.  