print("Enter '0' for exit.");
num = input("Enter any character or alphabet: ");
if num == '0':
    exit();
else:
    if((num>='a' and num<='z') or (num>='A' and num<='Z')):
    	print(num, "is an alphabet.");
    else:
    	print(num, "is not an alphabet.");
