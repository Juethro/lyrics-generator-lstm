# def pred(a):
#     b = predict(a)
#     return b

# for i in ['they', 'will', 'kill', 'crash', 'class']:
#     hasil = []
#     do = pred(i)
#     hasil.append(do)
#     print(hasil)
from predict import *
import json

def translate(inp1,inp2,inp3,inp4):
    hasil = []
    for i in [inp1,inp2,inp3,inp4]:
        lirik = predict(i)
        hasil.append(lirik)

    #menyiapkan json output
    out = {
        'out1': hasil[0],
        'out2': hasil[1],
        'out3': hasil[2],
        'out4': hasil[3]
        }
    # objectout = json.dumps(out, indent = 4)
    return out