''' password strength calculator '''
import string
import re

# pw = input('Enter Password: ')
pw = '124654545hgfhgfhjgf212464'
lenpw = len(pw)
up = sum(1 for u in pw if u.isupper())
lo = sum(1 for l in pw if l.islower())
num = sum(1 for n in pw if n.isnumeric())
sym = sum(1 for s in pw if not s.isalnum())


# scores
scochar = lenpw * 4
scocase = up * 2 + lo * 2
sconum = scochar
scosym = (lenpw - (scocase))

# penalties
if pw.isalpha() is True: ltronly = lenpw/3 
if pw.isnumeric() is True: numonly = lenpw/1.5 
if pw.isupper() is True: uponly = lenpw/2
if pw.islower() is True: loonly = lenpw/6.66 


print('password length = ', lenpw)
print('character score = ', scochar)
print()
print('upper letter count = ', up)
print('lower letter count = ', lo)
print('case score = ', scocase)
print()
print('numbers =', num)
print('symbols =', sym)
print()
# print(numb, type(alist[1]))
print(uponly)
print(loonly)
print()
print(ltronly)
print(numonly)

# myregex = r'8765@865.com'
