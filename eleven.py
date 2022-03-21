from itertools import groupby

def encode_bwt(text):
    text += '\0'
    table = sorted(text[i] + text[:i] for i in range(len(text)))
    last_colum = [row[-1] for row in table]
    return "".join(last_colum)

def decode_bwt(code):
    table = [""] * len(code)
    for i in range(len(code)):
        table = sorted(code[i] + table[i] for i in range(len(code)))
        s = [row for row in table if row.endswith('\0')][0]
    return s.rstrip('\0')

def rle_encode(text):
    return [(k, len(list(g))) for k, g in groupby(text)]


text = "i want home "
code = encode_bwt(text)
print(code)
print(decode_bwt(code))
print(rle_encode(text))