import re
str = "afdsfff,gfdgfdgf."

list =["asdfasdfads"]

list1  =str.split(',')

#print(list1)


dic = {"n":"I","k":"person name"}

#for i, value in dic:
 #   print(i)




def test():
    return "asdfasdfasdfasdf"



string = "asdfasdf.txt"

if string.endswith('.txt'):
    print(string)



def test3(*params):
    for item in params:
        print(item)

test3("adsfa","fff","fffeaff")


cx = 330



def getGroup(gen):

    for s in gen:
       s = re.split('[,，]',s)
       if s[-1] == '':
           s.pop()
    return s


'''
       for str in s:
           if str!='' and str!=' ':
               yield str.strip()
'''

#for i in getGroup(["asdfasdf,, adsfadf, asdfadf, , ,,,asdfasdf"]):
print( getGroup(["asdfasdf,, adsfadf, asdfadf, , ,,,asdfasdf"]))



def list_test1():
    stack = []
    stack.append("asdfasdf")
    stack.append("asdfad")
    stack.append("sdafasdf")
    return stack

s = list_test1()
print(s)