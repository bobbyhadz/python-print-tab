# How to print a Tab in Python 

string = 'bobby\thadz'
print(string)  # 👉️ bobby   hadz

print(repr('\t'))  # 👉️ '\t'

tab = '\t'

string = f'bobby{tab}hadz'
print(string)  # 👉️ bobby   hadz


first = 'bobby'
last = 'hadz'

print(first + '\t' + last)  # 👉️ bobby   hadz

print('a', 'b', 'c', sep='\t')  # 👉️ 'a       b       c'