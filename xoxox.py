class Main():
    def xoxo(str):
    	
    	countX=str.count('x')
    	countO=str.count('o')
    	if countO==countX:
    		print("true")
    	else:
    		print("false")
    userIn=input("please enter x and o as you want:")
    xoxo(userIn)
if __name__=="__main__":Main()


