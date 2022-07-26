'''This program module contains the conversion part where decimal numbers are converted into binary numbers. And after the conversion, the
   converted values are then reversed using for loop. Similarly, another function to check any numbers whether it was in range or not
   was used in this module.'''
#Pranjal Piya, 8th may, 2020
#function is called
#Conversion of Decimal number to Binary number
#while loop is used to carry out 8-digit binary number
def DTB(decimal_v):
           
           b_v=[]
           binary_v=[]
           count=0

           while count!=8:
                      remain = decimal_v%2
                      b_v.append(remain)
                      decimal_v=decimal_v//2 #quotient
                      count+=1


           #Reversing the output binary values using for loop                 
           for i in range(len(b_v)-1,-1,-1):
                    binary_v.append(b_v[i])
           return binary_v



#function is called
#using while loop to check whether the input is within the range or not
def check_num(n):
           while (n<0 or n>255):
                      print("***********************ERROR***********************")
                      n=int(input("It is not in range. Type again which range from 0-255: "))
                      print("\n")
           return n                      

#program closed




