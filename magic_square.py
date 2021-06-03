magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
raw1 = 0
raw2 = 0
raw3 = 0
colum1 = 0
colum2 = 0
colum3 = 0
dign = 0
dign2 =0
i = 0
while i<len(magic_square):
    j = 0
    while j<len(magic_square[i]):
        if raw1!=15:
            raw1+=magic_square[i][j]
        elif raw2!=15:
            raw2+=magic_square[i][j]
        else:
            raw3+=magic_square[i][j]
        j+=1
    i+=1
print(raw1,raw2,raw3)
a = 0
while a<len(magic_square):
    b = 0
    while b<len(magic_square[a]):
        if colum1!=15:
            colum1+=magic_square[b][a]
        elif colum2!=15:
            colum2+=magic_square[b][a]
        else:
            colum3+=magic_square[b][a]
        b+=1
    a+=1
print(colum1,colum2,colum3)
k = 0
while k<len(magic_square):
    l = k
    while l<len(magic_square[k]):
        dign+=magic_square[k][l]
        l+=3
    k+=1
print(dign)
length = len(magic_square)
n = 0
while n<len(magic_square):
    m = length-1
    while m>=1:
        dign2+=magic_square[n][m]
        m-=2
    length-=1
    n+=1
dign2+=magic_square[2][0]
print(dign2)
if raw1==raw2==raw3==colum1==colum2==colum3==dign==dign2:
    print("yes it is magic_square","👍")
else:
    print("no it is not magic square","👎")