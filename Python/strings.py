def quotify(quote, name):
    upper = "\"" + quote + "\""
    spaces = len(upper) - len("-" + name)
    return(upper + "\n" + " " * spaces + "-" + name)

print(quotify("deez nuts", "john"))