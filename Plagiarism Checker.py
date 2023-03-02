#Plagiarism Checker

from difflib import SequenceMatcher

with open('E:\Code Clause\datafile1.txt') as file1 , open('E:\Code Clause\datafile2.txt') as file2:
    f1data = file1.read()
    f2data = file2.read()
    percentage = SequenceMatcher(None, f1data, f2data).ratio()
    print('The Two Files are Matching upto {} percentage'.format(percentage*100))
    
    
#Output:
'''
The Two Files are Matching upto 32.81907433380084 percentage

'''