Lexical
```
    iden := [A-Za-z_]+

    num  := [0-9]+

    comment := --[^\n]*
```

Parser
```
    lp := |
        stmt lp
    
    stmt :=
        PUSH num    |
        LD num      |
        ST num      |
        PLUS        |
        MIN         |
        MUL         |
        DIV         |
        PER         |
        PRINT
```