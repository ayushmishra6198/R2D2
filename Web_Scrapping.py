from bs4 import BeautifulSoup
import requests
import json
import re
 
def GetData(number):
    #print(number)
    #print((number*250)+1)
    fileToWrite = open("data.txt","a+")
    url = 'https://www.imdb.com/search/title?title_type=feature,tv_movie&colors=color,black_and_white&count=250&start={0}&ref_=adv_nxt'.format(
        str((number*250)+1))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    defautUrl = "https://www.imdb.com"
 
    # Movie Container List
    movie_Container = soup.find_all('div', class_="lister-item mode-advanced")
    for movie in movie_Container:
        # Get name of movie
        name = movie.h3.a.text
        # Get Movie Url
        #movieUrl = defautUrl + movie.h3.a["href"]
        # Now Find Year
        year = movie.h3.find('span', class_="lister-item-year text-muted unbold")
        yearOfRelease = year.text
        # Now check the disc
        #Desc = movie.find_all('p', class_="text-muted")[1].text
        # Now Some More Data
        #MovieData = movie.find_all('p', class_="text-muted")[0].text
        # Star Rating Can be None
        StarRating = "N/A"
        try:
            StarRating = movie.find('div', class_="inline-block ratings-imdb-rating")['data-value']
        except:
            StarRating = "N/A"
        # MetaScore
        #MetaScore = "N/A"
        #try:
        #    MetaScore = movie.find('span', class_="metascore favorable").text
        #except:
        #   MetaScore = "N/A"
        # Votes count
        #Votes = "N/A"
        #try:
        #    Votes = movie.find('span', attrs={'name': 'nv'})['data-value']
        #except:
            continue
        # For Director and Star Cast
        ListerItem = movie.find('div',class_='lister-item-content')
        getAllPTags = ListerItem.find_all('p')
        CastString = getAllPTags[2].text
        movieDump = {
            "name":name,
            #"movieUrl":movieUrl,
            "YOR":yearOfRelease,
            #"desc":Desc,
            #"movieData":MovieData,
            "starCast":CastString,
            "starRating":StarRating,
            #"metaScore":MetaScore,
            #"voteCount":Votes
        }
        fileToWrite.write(json.dumps(movieDump)+","+"\n")
    fileToWrite.close()
 
def main():
    number = 4
    for x in range(0,number+1):
        GetData(x)
    print('done check data.csv file')
 
if __name__ == '__main__':
    main()
