# random-string
Generates a random string of a specified length.

# Usage
Currently there are 5 types:
- uppercase
- lowercase
- upperlower
- alphanumerical
- ascii

You can probably guess what each one would create

The function requires 2 parameters type and length; Type of course is the above.
```py
RandString(type, length)
```
Now lets look at some examples

uppercase:
```py
print(RandString("uppercase", 10))
# Output: TPDROEAVRY
```

lowercase:
```py
print(RandString("lowercase", 10))
# Output: mdvsewzkwf
```

upperlower:
```py
print(RandString("upperlower", 10))
# Output: YjHFGzysFx
```

alphanumerical:
```py
print(RandString("alphanumerical", 10))
# Output: Fy0Nbqno6B
```

ascii:
```py
print(RandString("ascii", 10))
# Output: jtj-NV<PSV
```