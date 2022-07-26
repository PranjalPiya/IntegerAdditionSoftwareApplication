'''This program is refered as main part of whole program. This module takes two integer values from the user, and when the user input
   values that exceed the limit the program will run again. This module keeps on executing until the user wishes. All the sub modules
   were also imported here. '''
#Pranjal Piya, 8-may, 2020
#importing different sub modules to the main module
import conversion
import list_to_string as list_s
import bitadder

#Beginning part of the program.
print("\n")
print("***** Welcome to the Program******")
print("\n")

invalid=False
continue_=True


#while loop is used
while continue_==True:
           #Exception handling using try except
           try:
                      #for the first decimal number
                      first_num = int(input("Enter the first decimal number: "))
                      first_num=conversion.check_num(first_num)
                      a=conversion.DTB(first_num)
                      c=list_s.LTS(a)
                      

                      #for the second decimal number
                      second_num = int(input("Enter the second decimal number: "))
                      second_num=conversion.check_num(second_num)
                      b=conversion.DTB(second_num)
                      d=list_s.LTS(b)
                      print("\n")

           except:
                      #when user input other values like alphabets or symbols except numberic values.
                      print("\n")
                      print("<<<<<<Error>>>>>>")
                      print("The inserted value is invalid. Please re-type again.")
                      print("<<<<<<Error>>>>>>")
                      print("\n")
                      continue
           
                      

           #printing the conversion of decimal number to binary number
           print("The Binary conversion of",first_num,"=",c)
           print("The Binary conversion of",second_num,"=",d)

           #Binary addition part           
           if invalid==False:
                      
                      x=bitadder.bit_adder(a,b)
                      if (first_num+second_num)>255:
                                 print("")
                                 print("Error.! The sum of inserted value is greater than range 0-255.")
                                 print("\n")
                                 continue
                      else:
                                 
                                 y=list_s.LTS(x)
                                 print("The Binary addition of",first_num,"and",second_num,"=",y)
                                 
                      
           #checking whether the users still want to run program or not
           print("***********************************************")
           run=input("Do you still want to run the program..? Type 'Yes' or 'No' :")
           print("***********************************************")
           print("\n")
           if run=="No":
                      continue_=True
                      print("****Thank you****")
                      print("\n")
                      break
           
#program closed
