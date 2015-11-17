from bs4 import BeautifulSoup
from urllib2 import urlopen

countries = {}
url = "http://hypem.com/blogs/country/US"


def get_blogger_list(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    #more code here
