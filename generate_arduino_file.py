def generate_arduino(path_out, morse_string):
    path = ".arduino/to_generate.ino"
    with open(path, "r") as f:
        txt = "".join(f.read()).replace('&morse&', morse_string)
    with open(path_out, "w") as f:
        f.write()



path = ".arduino/to_generate.ino"
morse = "- .... .. ... / .. ... / .- / -- . ... ... .- --. . / ... . -. -.. . -.. / - --- / --. . -. . .-. .- - . / .- .-. -.. ..- .. -. ---"

out = generate_arduino(path, morse)
print(out)