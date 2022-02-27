# Life Path

Description
```
    PUSH (n) : number push last of stack
    PLUS : replace 2 last element of stack with result of sum
    MIN : replace 2 last element of stack with result of mines
    MULT : replace 2 last element of stack with result of multipy
    DIV : replace 2 last element of stack with result of division
    PRINT : print of last element on stack
    ST (src) : pop last item and set data to source index 
    LD (src) : get data in source index and push to last element
```

Code [**Test Case 0**](https://github.com/NIT98/lifepath/test/0)<br>
```
    PUSH 7
    PUSH 3
    PUSH 8
    PLUS   
    LD   0
    MUL
    PRINT
```
Stack 
```
    [7]
    [7, 3]
    [7, 3, 8]
    [7, 11]
    [7, 11, 7]
    [7, 77]
    77
    [7]
```

Code [**Test Case 1**](hhttps://github.com/NIT98/lifepath/test/0)<br>
```
    PUSH 2
    PUSH 3
    PLUS
    PRINT
```
Stack
```
    [2]
    [2, 3]
    [5]
    5
    []
```