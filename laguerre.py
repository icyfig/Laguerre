# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:24:16 2021

IMPORTANT: 
1. The variable of the input polynomial must be 'y' not 'x'
2. All terms of the input polynomial must be seprated by '+' not '-'. 
For example, write, 'y + -3' instead of 'y - 3'
3. Spaces do not matter

Sample Runs

please enter the polynomial in the form ( 3y**3 + -5y**4 + 30) : 3y**2+6y+2
root = -0.42264973081037516

please enter the polynomial in the form ( 3y**3 + -5y**4 + 30) : y**2+8y+12
root = -2.0

please enter the polynomial in the form ( 3y**3 + -5y**4 + 30) : 4
root = 4

please enter the polynomial in the form ( 3y**3 + -5y**4 + 30) : 4y**5+6
No real roots exist


"""



def find_derivative(B):
   while '+' in B :
      index = B.index('+')
      B = B.replace('+' , ' ' )
   B = B.split()
   B_drv = []
   
   counter=0
   for i in B:
      if 'y' in i:
         #print("i = = " +str(i))
         index_y = i.index('y')
         multiply = i[0:index_y]
         if multiply == '' :
            B[counter]= '1'+B[counter]
         if multiply == '-':
            B[counter]= '-1'+B[counter][1:]
      counter += 1

   def deriv(B):
       for parameter in B :
           if 'y' in parameter :
               index_y = parameter.index('y')
               multiply = parameter[0:index_y]

               if multiply == '' :
                   multiply = '1' 
               if multiply == '-':
                  multiply = '-1'
               power = parameter[index_y+3:]
               if(power == ''):
                  power = 1

               if power != '0' :
                   #print("power = "+str(power)+ " multiply = " +str(multiply))
                   drv_parameter = str(float(multiply) * float(power)) + 'y**' + str(float(power)-1) 
               else :
                   drv_parameter = str(0) #in case the user wrote a parameter '4y**0' instead of '4'
               B_drv.append(drv_parameter)
           else:
               drv_parameter = str(0)
               B_drv.append(drv_parameter)
       result = ' + '.join(B_drv)
       return result
   
   
   return deriv(B)

def plug_value(B,y_value):
   y_value = str(y_value)
   while '+' in B :
      index = B.index('+')
      B = B.replace('+' , ' ' )
   B = B.split()
   
   counter=0
   for i in B:
      if 'y' in i:
         #print("i = = " +str(i))
         index_y = i.index('y')
         multiply = i[0:index_y]
         if multiply == '' :
            B[counter]= '1'+B[counter]
         if multiply == '-':
            B[counter]= '-1'+B[counter][1:]
      counter += 1
         
   
   def calc_deriv(B_drv, y_value):
#      print("yvalue ---------------------> " + str(y_value))
      for parameter in B_drv :
#         if 'y' in parameter :
#            index_y = parameter.index('y')
#            multiply = parameter[0:index_y]
#            if multiply == '' :
#               parameter= '1'+parameter
         index_parameter = B_drv.index(parameter)
         #print("bdrv ===========  "+str(B_drv[index_parameter]))
         B_drv[index_parameter] = parameter.replace('y' , '*' + y_value ) # to replace '4y**3' with '4*number**3'
         #print("2. bdrv ===========  "+str(B_drv[index_parameter]))
         
         B_drv[index_parameter] = str(eval(B_drv[index_parameter]))
      result = eval(' + '.join(B_drv))
      return(result)
       
   return calc_deriv(B,y_value)

def get_degree(B):
   while '+' in B :
      index = B.index('+')
      B = B.replace('+' , ' ' )
   B = B.split()
   degree=0
   for parameter in B :
      if 'y' in parameter :
         index_y = parameter.index('y')
         power = parameter[index_y+3:]
         if(power == ''):
            power = 1
         #print("Power ==== "+str(power))
         if(int(power)>degree):
            degree = int(power)
   return degree

#4y**5+6
#y**2+8y+12
#3y**2+6y+2
#-3y**3+-y+-57
   

def main():
   B = input('please enter the polynomial in the form ( 3y**3 + -5y**4 + 30) : ')
   B = B.replace(' ' , '')
   JobDone = False
   if('y' not in B):
      print("root = " +str(B)) #If it is a constant, then the constant is the root
      JobDone = True
   #print(find_derivative(B))
   #print(plug_value(find_derivative(B),1))
   x = 2 #initialGuess
   k=0
   realroots=True
   if(JobDone == False):
      n = int(get_degree(B))
      if(n==0): #If degree is zero, then the input is the root
         print("root = "+str(B))
         quit()
   #print("degree = "+str(n))
   max_loops = 10000
   while(k<=max_loops):
      #print("x= "+ str(x))
      if(JobDone == True):
         break
      px = plug_value(B,x)
      #print("px="+str(px))
      if(abs(px)<0.000001):
         break
      
      p1 = find_derivative(B)
      p2 = find_derivative(p1)
      
      px1 = plug_value(p1,x)
      px2 = plug_value(p2,x)
      
      g = px1/px
      
      h = g**2 - (px2/px)
      
      #finding a
      a=0
      if((n-1)*(n*h-g*g)<0):
         print("No real roots exist")
         realroots=False
         break
      den_root = ((n-1)*(n*h-g*g))**(0.5)
#      print("den_root_before_root"+str((n-1)*(n*h-g*g)))
      den_plus = g + den_root
#      print("den_plus    "+str(den_plus))
      den_minus = g - den_root
#      print("den_minus    "+str(den_minus))
      if(abs(den_plus)>abs(den_minus)):
         a=n/(den_plus)
      else:
         a=n/(den_minus)
      #print("a---------------->" +str(a) )
      x = x-a
      k += 1    
   
   if(realroots and not JobDone):
      print("root = "+str(x))
   
   
main()
