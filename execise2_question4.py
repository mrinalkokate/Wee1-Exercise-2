# -*- coding: utf-8 -*-
"""execise2-Question4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CgYcES7ZhB_-ClHc_m7GgadLDHDffL-D
"""

Write a program that prompts the user for the user for their five favourite movies. Store each
movie in a list. If the user at any stage enters Quit at any stage, the program should stop
prompting the user for the movie name and should print to the screen the movies captured in
the list up to that point.

print("_____________________________________")
print("WELCOME TO MY FAVOURITE MOVIES LIST")
print("_____________________________________")
movies=[]
while True:
  movie=input("Enter your favourite movie in the list")
  movies.append(movie)

  user_input=input("Do you want to add more movies? Yes/No")
  if user_input=='no' or user_input=='NO' or user_input=='quit' or user_input=='n' or user_input=='No':
    break

print("Below is the list of my favourite movies")
print(movies)
print("____________________________________________")
print("Thats the end of the program, see you soon")
print("____________________________________________")