# !Python
 
# Chapter 4 practice projects
 
def eggs(listvalue):
    for i in range(len(listvalue)):
        print(listvalue[i] + ', ', end="")
        if listvalue[i] == listvalue[-2]:
            print('and ' + listvalue[-1], end="")
            break
 
 
spam = ['apples','bananas','tofu','cats']
eggs(spam)
