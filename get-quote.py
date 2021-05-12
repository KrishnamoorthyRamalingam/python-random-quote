def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
#  print(quotes[0])
  print(rnd)
  print(quotes[rnd])


# print(quotes)
import random

if __name__== "__main__":
  primary()
