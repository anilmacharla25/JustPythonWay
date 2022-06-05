str1=input('enter the string:')
shift_value=int(input("enter the value:"))
new_str=""
# str1=str1.replace(" ",'')
# print(str1)
for i in str1:
    i=i.lower()
    # print(i)
    new_str=new_str+i
# print(new_str)
encripted_str=""
for i in new_str:
    # print(ord("z"))
    if ord(i)>=120:
        mod_asci=ord(i)-26
        # if ord(i)==
        asci_value=mod_asci+shift_value
        # print(ord())
        # print(chr(asci_value))
        encripted_str=encripted_str+chr(asci_value)
    else:
        asci_value=ord(i)+shift_value
        # print(ord())
        # print(chr(asci_value))
        encripted_str=encripted_str+chr(asci_value)   
print(encripted_str.replace("$"," "))
