import sys
import argparse
from colorama import Fore, Back, Style
from colorama import init
init()






def names(fname, lname):
      print("names permutation which are possible")  


def Head(string):
   print(Fore.GREEN + "#########----- "+string+" -----#########")

def Sub(string):
  print(Fore.BLUE+"[][]", end =" "),
  print(Fore.WHITE +string+" ")

def message(string):
   print(Fore.RED+"*** "+string+" ***")



try:
   lable = sys.argv[1]
except:
   message("Arguments Required , Please -h for further help")
   sys.exit()


if lable == '-h':
  Head("Use the following syntax to run this program")
  Sub(" -n   [value] in for only one name")
  Sub(" -fl  [value] [value2] for first name and last name")
  Sub(" -h  for help ")
  Sub(" -f   for fb only")
  Sub(" -t   for twiiter enum only")
  Sub(" -a   for all ") 
  sys.exit()


if lable == '-fl':
   firstname = sys.argv[2]
   lastname = sys.argv[3]

   names(firstname,lastname)		
   print(" ")


  

elif lable == '-n':
  name = sys.argv[2]
  print(name)



   