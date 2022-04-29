def generate_arduino():

    lst = [0,0,1,1,1,0,0]

    f = open("arduino/to_generate.ino", "r")
    texto = f.read()
    texto.replace("a", "AAA")
    return(texto)

print(generate_arduino())