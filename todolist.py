

list=[]
def add():
    dict={}
    
    try:
        name=str(input("name:"))
        age=int(input("age:"))
        dict["name"]=name
        dict["age"]=age
        list.append(dict)
        return
    except:
        print("an error")
def update():
    old_name=str(input("old name:"))
    old_age=int(input("old age:"))
    for i in list:
        
            if i["name"]==old_name and i["age"]==old_age:
                new_name=str(input("new name:"))
                new_age=int(input("new age:"))
                
                i["name"]=new_name
                i["age"]=new_age
                return

            
            print("didnt exist")
def delete():
    old_name=str(input(" name:"))
    old_age=int(input(" age:"))
    for i in list:
        
            if i["name"]==old_name and i["age"]==old_age:
                
                
                del i["name"]
                del i["age"]
                return

            
            print("didnt exist")

def show():
    global list
    for i in list:
        for i,j in i.items():
            print(i,j)


def start():
    msg="""
what do you want:
1-add
2-update
3-delete
4-show all
5-exit
"""
    while True:
        ask_user=int(input(msg))
        if ask_user==1:
            add()
        elif ask_user==2:
            update()
        elif ask_user==3:
            delete()    
        elif ask_user==4:
            show()
        elif ask_user==5:
            print("good bye -_-")
            return
            
            
    

if __name__=="__main__":
        
    start()  
    