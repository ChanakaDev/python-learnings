'''
===========================
(L)(E)(G)(B) Rule
===========================

-   Local (or function) scope: 
-------------------------------
    * is the code block or body of any Python function or lambda expression.

-   Enclosing (or nonlocal) scope: 
-------------------------------
    * is a special scope that only exists for nested functions. 
    * If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. 

-   Global (or module) scope: 
-------------------------------
    * contains all of the names that you define at the top level of a program or a module.
    * define outside of all the classes and functions. 

-  Built-in scope
-------------------------------
    * is a special Python scope that is created or loaded whenever you run a script or open an interactive session. 

LEGB Rule
-------------------------------
    * Python will look that name up sequentially in the local, enclosing, global, and built-in scope. 
        * If the name exists, then you will get the first occurrence of it. 
        * Otherwise, you will get an error.   

Short Note
-------------------------------
(*) Local       : variable inside a fun() body
(*) Global      : variable outside of all the fun() and classes  
(*) Enclosing   : nested fun(), innermost can access outer fun() variables, but not vice versa
(*) Built-in    : accessibility of built-in keywords/ functions without defininig 
'''