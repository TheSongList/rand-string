import random as rand

def RandString(type, length):
    length = int(length)
    if length <= 0: raise Exception("Invalid length in RandString({}, {})".format(type, length))
    if type == "uppercase":
        response = ""
        for i in range(length):
            code = rand.randint(65, 90)
            response += chr(code)
        return response

    elif type == "lowercase":
        response = ""
        for i in range(length):
            code = rand.randint(97, 122)
            response += chr(code)
        return response

    elif type == "upperlower":
        response = ""
        code = 0
        for i in range(length):
            choice = rand.randint(0, 1)
            if choice == 0: code = rand.randint(65, 90)
            else: code = rand.randint(97, 122)
            response += chr(code)
        return response

    elif type == "alphanumerical":
        response = ""
        code = 0
        for i in range(length):
            choice = rand.randint(0, 2)
            if choice == 0: code = rand.randint(65, 90)
            elif choice == 1: code = rand.randint(97, 122)
            else: code = rand.randint(48, 57)
            response += chr(code)
        return response
        
    elif type == "ascii":
        response = ""
        for i in range(length):
            code = rand.randint(33, 126)
            response += chr(code)
        return response
    else: raise Exception("Invalid type in RandString({}, {})".format(type, length))
