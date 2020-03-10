morsecode={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..',
'j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-',
'u':'..-','v':'.---','w':'.--','x':'-..-','y':'-.--','z':'--..'}
def get_key(val):
    for key,value in morsecode.items():
        if val==value:
            return key
        return None
ch=input('enter choice 1.m-a 2.a-m')
if ch=='1':
    string=[]
    string= input().split(' ')
else:
    string = input()

for i in range(len(string)):
    if ch=='2':
        print(morsecode.get(string[i]),end=' ')
    elif ch=='1':
        print(list(morsecode.keys())[list(morsecode.values()).index(string[i])],end='')

