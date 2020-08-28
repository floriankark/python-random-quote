import random

def prime():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0,last)
  mltpl = random.randint(0,last-rnd)
  while mltpl >= 0:
      print(quotes[rnd + mltpl])
      mltpl -= 1

if __name__== "__main__":
  prime()
