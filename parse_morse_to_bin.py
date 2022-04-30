def morse_to_bin(string):
    res = ""
    for ch in string:
            if ch == ' ':
                res.join("000")
            elif ch == '/':
                res.join("000000")
            elif ch == '.':
                res.join("1")
            elif ch == '-':
                res.join("111")
    print(res)

print(morse_to_bin("-- .- .-. .. .- -. .- / . ... - .- / .- --.- ..- .. / -.-. --- -- .. --. ---"))
