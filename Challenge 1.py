a = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'''
#a = '''www.pythonchallenge.com/pc/def/map.html'''
b = 'abcdefghijklmnopqrstuvwxyz'

c = ''

for i in a:
    s = 0
    for j in b:
        s = s + 1
        if i == j:
            if s < len(b) - 2:
                i=b[s+1]

            if s == len(b) - 1:
                i=b[0]

            if s == len(b):
                i=b[1]

            break

    c = c + i

#c.maketrans()

print (c)
