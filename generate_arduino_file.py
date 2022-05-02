import os

def generate_arduino(file_name, morse_string):
    origin = "arduino/to_generate.ino"

    # ler e substituir no texto do arquivo aberto
    with open(origin, "r") as f:
        txt = "".join(f.read()).replace('&morse&', morse_string)
        f.close()
    
    # verificar se out/ existe
    if not os.path.exists(".out/"):
        os.mkdir(".out/")

    # escrever o arquivo de saida
    with open(".out/"+file_name, "w") as f:
        f.write(txt)
        f.close()

    # log
    print("\n\"Arquivo salvo com sucesso! Acesse 'out/'\"")