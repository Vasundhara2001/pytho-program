# Declare a variable and initialize it  
x = 101 
name= 'parth'
  
# Global variable in function  
def mainFunction(): 
    #name = "parth" 
    # printing a global variable  
    global x  
    global name
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Javatpoint'  
    print(x)  
    print(name)
  
mainFunction()  
print(x)  
print(name)