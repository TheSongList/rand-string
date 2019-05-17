# rand-string
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
import rand_string.rand_string as rand
rand.RandString(type, length)
```
Now lets look at some examples

uppercase:
```py
print(rand.RandString("uppercase", 10))
# Output: TPDROEAVRY
```

lowercase:
```py
print(rand.RandString("lowercase", 10))
# Output: mdvsewzkwf
```

upperlower:
```py
print(rand.RandString("upperlower", 10))
# Output: YjHFGzysFx
```

alphanumerical:
```py
print(rand.RandString("alphanumerical", 10))
# Output: Fy0Nbqno6B
```

ascii:
```py
print(rand.RandString("ascii", 10))
# Output: jtj-NV<PSV
```