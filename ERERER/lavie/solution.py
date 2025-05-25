def postfix_to_infix(query):
    stack = []
    i = 0
    j = 1
    typ = query[0] - 17
    infix = ""

    while True:
        match typ:
            case 0:
                stack.append(str(query[j]))
                j += 1
            case 1:
                infix = stack.pop()
            case 2:
                u = stack.pop()
                v = stack.pop()
                result = f'{v} * {u}' 
                stack.append(result)
            case 3:
                u = stack.pop()
                v = stack.pop()
                result = f'{v} + {u}' 
                stack.append(result)
            case 4:
                print(infix)
            case 5:
                stack.append(f'a{i}')
            case 6:
                u = stack.pop()
                v = stack.pop()
                result = f'({v} >> {u} & 1)' 
            case 7:
                u = stack.pop()
                v = stack.pop()
                result = f'({v} ^ {u})' 
                stack.append(result)
            case 8:
                i += 1
            case 9:
                break
            case _:
                print("Unknown case type")
                break
        
        typ = query[j] - 17
        j += 1
        if j >= len(query):
            break

    return infix


def evaluate_infix(infix):
    a = infix.split(") + (")
    i = 0  
    while i < 32:
        val = 33  
        while val < 128:
            s = a[i].replace(f'a{i}', str(val))  
            if i == 0:
                s += ')'
            elif i == 31:
                s = '(' + s
            try:
                if eval(s) == 0: 
                    print(chr(val), end='')  
                    break
            except:
                pass 
        
            val += 1  
        i += 1 


def main():
    query = open("command", "rb").read()  #mở ở binary mode
    infix = postfix_to_infix(query)
    print("Final Infix Expression:", infix)
    evaluate_infix(infix)


if __name__ == "__main__":
    main() 

