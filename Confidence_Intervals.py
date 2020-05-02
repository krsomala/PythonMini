#a simple program to find confidence intervals of a list of values
import numpy as np
ch = input("Enter 1 to give values and 2 if you already have mean and sd:  ")
if ch=='1':
    values = list(map(float,input().split(',')))

else:
    n = int(input("enter length of sample: "))
    x = float(input("enter mean: "))
    s = float(input("Enter sd: "))
percent = input("Enter the percentage of confidence to be calculated: ")
if percent=='85':
    z=1.440
elif percent=='90':
    z=1.645
elif percent=='95':
    z=1.960
elif percent=='99':
    z=2.576
else:
    print('enter a valid percentage of confidence')
if ch=='1':
    x=np.mean(values)
    s=np.std(values)
    n= len(values)
Con_Int_0 = x - z*(s/np.sqrt(n)) 
Con_Int_1 = x + z*(s/np.sqrt(n))
print('the {}% confidence interval of the given values is between {} and {}'.format(percent,Con_Int_0,Con_Int_1))
