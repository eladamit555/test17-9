def camel_to_hyphen(text:str) -> str:
    result = ''
    for c in text:
        if c.isupper():
            result += '-' + c.lower()
        else:
            result += c
    return result
print(camel_to_hyphen('helloPython'))
print(camel_to_hyphen('python'))
print(camel_to_hyphen('aBigTest'))