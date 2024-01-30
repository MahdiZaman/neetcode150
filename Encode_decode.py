"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    res = ''
    for s in strs:
        encoded = str(len(s)) + '/' + s
        res += encoded
    return res

def decode(strs):
    res = []
    i = 0
    while i < len(strs):
        e = i
        while e < len(strs) and strs[e] != '/':
            e += 1
        size = int(strs[i:e])
        word = strs[e+1: e + 1 + size]
        i = e + 1 + size
        res.append(word)
    return res
        
    

if __name__=='__main__':
    strs = ['Hello', 'World', 'Python']
    encoded = encode(strs) # '5/Hello5/World6/Python'
    print(f'encoded: {encoded}')
    
    decoded = decode(encoded)
    print(f'decoded: {decoded}') # ['Hello', 'World', 'Python']