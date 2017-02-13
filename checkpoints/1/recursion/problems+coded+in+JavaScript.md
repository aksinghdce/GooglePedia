
# Modular expression: pow(A,B)%C


```javascript
function modEx(A, B, C, mul=1) {
    if(B == 0) {
        if(C == 1) {
            return 0;
        }else {
            return 1;
        }
    }
    
    if(B == 1) {
        console.log((mul*A)%C);
        return (mul*A)%C;
    }
    
    //Simplify multiple
    if(mul > C) {
        mul = mul%C;
    }
    
    modEx(A, B-1, C, mul*A);
}
```




    undefined




```javascript
modEx(25, 304, 7);
```

    4





    undefined


