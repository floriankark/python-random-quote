import random

def prime():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(1,13)

  print(quotes[rnd])

if __name__== "__main__":
  prime()
