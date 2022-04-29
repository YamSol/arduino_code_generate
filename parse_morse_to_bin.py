def morse_to_bin(string):
    res = []
    for ch in string:
            if ch == '/':
                res.append(000)
            elif ch == '0':
                res.append(0)
            elif ch == '1':
                res.append(1)
    print(res)

morse_to_bin("--- .-.. .- / -.- .- .-. .-.. --- ...")
