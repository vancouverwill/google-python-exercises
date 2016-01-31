import sys

def main():
  words = ['cat', 'window', 'defenestrate']
  for w in words:
    print w, len(w)

  for num in range(5, 10):
      print 'num-' + str(num)


        # This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()