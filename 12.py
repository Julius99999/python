t=('python','hello','world')
print(t[0])
t2=t[0:3:2]
print(t2)


for item in t:
    print(item)


for i in range(len(t)):
    print(t[i])












d={10:'cat',30:'dog',20:'zoo'}
print(d)


lst1=[10,20,30,40]
lst2={'cat':'dog','zoo':'cat'}
zipobj=zip(lst1,lst2)
print(zipobj)

d=dict(zipobj)
print(d)

d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t:10})

print('max:',max(d))
print('min:',min(d))
print('len:',len(d))