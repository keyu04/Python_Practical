#10 Define a procedure histogram () that takes a list of integers and prints a histogram to the 
#screen. For example, histogram ([4, 9, 7]) should print the following:
#****
#*********
#*******

def histogram( items ):
    for n in items:
        output = ''
        t = n
        while( t > 0 ):
          output += '*'
          t = t - 1
        print(output)

histogram([4,9,7])
