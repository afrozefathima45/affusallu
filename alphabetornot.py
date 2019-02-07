num = input()
if num == '0':
    exit()
else:
    if((num>='a' and num<='z') or (num>='A' and num<='Z')):
    	print( "Alphabet")
    else:
    	print("No")
