import random

def prime():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
<<<<<<< HEAD
  rnd = random.randint(0,last)
  mltpl = random.randint(0,last-rnd)
  while mltpl >= 0:
      print(quotes[rnd + mltpl])
      mltpl -= 1
=======
  rnd = random.randint(1,13)

  print(quotes[rnd])
>>>>>>> 844fd353669858bcf4facd1b6560e99e101d4647

if __name__== "__main__":
  prime()
