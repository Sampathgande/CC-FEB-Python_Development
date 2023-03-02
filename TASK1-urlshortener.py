#URL Shortener.py
import pyshorteners
url = input("Enter Url to shorten: ")

def shortenurl(url):
    short = pyshorteners.Shortener()
    print("Your shortned Url is: ",short.tinyurl.short(url))

shortenurl(url)

#Output:
'''
Enter Url to shorten: https://docs.python.org/3/library/tkinter.html#module-tkinter
Your shortned Url is: https://tinyurl.com/2eblt8ye
'''
