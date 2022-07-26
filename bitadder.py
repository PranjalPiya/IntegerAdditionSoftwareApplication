'''This sub module program contains the addition part of the main program in which addition is done using different kinds of logic
   gates. The gates which were used in the program are OR gate, AND gate and XOR gate. '''
#Pranjal Piya, 8-may, 2020
#function is called
#addition is done for 8-bit adder using different kinds of gates
#for loop is used 
def bit_adder(a, b):
           c=[0,0,0,0,0,0,0,0]
           add=[]
           reverse=[]
           for i in range(8):
                      sum=a[7-i]^b[7-i]^c[7-i]
                      c[(7-i)-1]=(c[7-i] and (a[7-i] ^ b[7-i]) or (a[7-i] and b[7-i]))
                      add.append(sum)
           for i in range(len(add)-1,-1,-1):
                      reverse.append(add[i])
           return reverse

#code closed


