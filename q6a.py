name=input("enter file name")
with open(name,mode='r') as f:
    lines=f.readlines()
    n=int(input("enter no of lines"))
    for each in lines[:n]:
        print(each)
    c=0
    word=input('enter search word')
    for each in lines:
        c+=each.split().count(word)
    print("Word occurs",c,"times")