# -*- coding: utf-8 -*-
"""Exercise2-Question 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OvnP3XCNPNIt1AiXcEUCkKL9ggMGA1gp
"""

Suppose you shop for rice in two different packages. You would like to write a program to
compare the cost. The program prompts the user to enter the weight and price of the each
package and displays the one with the better price.

print("*************************************************")
print("PROGRAM TO COMPARE THE BEST PRICE OF THE RICE!!!")
print("*************************************************")
while True:
  x1=float(input("Enter the Weight of the Rice"))#input for the weight of 1st sample
  y1=float(input("Enter the price of the Rice"))#input for the price of 1st sample
  price1=x1*y1

  x2=float(input("Enter the Weight of the 2nd Rice"))#input for the weight of 2nd sample
  y2=float(input("Enter the price of the  2nd Rice"))#input for the price of 2nd sample
  price2=x2*y2

  if (price1>price2):
    print("The price is better for 2nd Rice")
  elif(price1<price2):
    print("The price for option 1 of Rice is better")
  elif(price1==price2):
    print("The prices are equal for both the varieties of rice")

  user_input=input("Do you want to try a different variety of Rice? - Yes/No ?")
  if user_input=='NO' or user_input=='no' or user_input=='n' or user_input=='No':
      break
print("***************************************************************************")
print("Thank you for using the Program for comparing the prices of the rice!!!")
print("***************************************************************************")