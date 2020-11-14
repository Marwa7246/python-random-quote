import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt","a+")
  for i in range(2):
       f.write("Appended line %d\r\n" % (i+1))
       
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) -1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)

  # print(quotes[last],quotes[rnd], end="")

  tmp = random.sample(quotes, 2)
  for i in tmp:
    print(i, end="")

if __name__== "__main__":
  primary()
