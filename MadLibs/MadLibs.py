from ast import FloorDiv
from random import randint
import copy

print("Welcome to MadLibs with lyrics")

Player = input("finish these Libs if you dare!")

if Player.lower() != "yes":
    quit()

print("Here are some libs: \n")


noun1 = input("enter a Noun: ")
noun2 = input("enter another Noun: ")
noun3 = input("enter another Noun: ")
place = input("Enter your favorite place in the world!")
adjective1 = input("enter an adjective!")
adjective2 = input("enter another adjective!")
adjective3 = input("enter another adjective!")
adverb1 = input("enter an adverb!")
adverb2 = input("enter another adverb!")
emotion = input("how are you feeling right now?")

print("so it goes on and on and on it's" + noun1 + "and" + noun2 + "oh well"
           "the lover of lifes not a" + noun3 + "the ending is just the " + place + "the closer you get to the"
           + adjective1 + "the sooner you know that your" + adjective2 + "so its on and on and on oh it's on and on and on it goes on and on"
           + adjective3 + "and" + adverb1 + "Oh I can" + adverb2 + "fool fool" "they say that lifes a" + emotion + "spinning fast you gotta ride it well"
           "the world is full of kings and queens who blind your eyes and steal your dreams it's" + noun1 + "and" + noun3)