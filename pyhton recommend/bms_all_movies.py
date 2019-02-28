#import the library used to query a website
import urllib.request

#specify the url
bms="https://in.bookmyshow.com/movies"

#Query the website and return the html to the variable 'page'
page=urllib.request.urlopen(bms)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, features="html.parser")

#print (soup.prettify)
#soup.find('div', id="widget-content")
wc=soup.find_all("div", class_="card-title") 

print(wc)
#latest_movie_list=[]
#latest_movie_links=[]
for div in wc: 

    h4=div.find("h4")
    #print(h4.text)
    #links=div.find("a")
    #links2=links.get('href')
    #latest_movie_links.append("https://in.bookmyshow.com"+links2)
    #latest_movie_list.append(h4.text)
    

#print(latest_movie_list)
#print(latest_movie_links)
        

#import pandas to convert list to data frame
#import pandas as pd

#df=pd.DataFrame(latest_movie_list,columns=['Trending Searches'])
#df['Links']=latest_movie_links

#print(df)
#df.to_csv(r'C:\Users\rohan\Desktop\pyhton recommend\trending_movies.csv', sep='\t', encoding='utf-8')