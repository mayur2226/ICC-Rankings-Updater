from flask import Flask , render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
    


@app.route("/")
def hello():
    URL='https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting'
    page= requests.get(URL)
    first=BeautifulSoup(page.content, 'html.parser')
    results=first.find(id='page-wrapper')
    fffs=results.find_all('div', class_='cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')
    
    ra=[]
    na=[]
    co=[]
    rat=[]
    
    for fff in fffs:
        ra.append(fff.find('div', class_='cb-col cb-col-16 cb-rank-tbl cb-font-16').get_text())
        na.append(fff.find('a', class_='text-hvr-underline text-bold cb-font-16').get_text())
        co.append(fff.find('div', class_='cb-font-12 text-gray').get_text())
        rat.append(fff.find('div', class_='cb-col cb-col-17 cb-rank-tbl pull-right').get_text())
        if None in (ra, na, co,rat):
            continue

    ran=ra[0:100]
    nam=na[0:100]
    coun=co[0:100]
    rati=rat[0:100]
    rank=ra[100:200]
    name=na[100:200]
    count=co[100:200]
    ratin=rat[100:200]
    rank1=ra[200:300]
    name1=na[200:300]
    countr=co[200:300]
    rating=rat[200:300]

            

        
     
    return render_template("index2.html", ra=ra,na=na,rat=rat,
    co=co,ran=ran,nam=nam,coun=coun,rati=rati,
    rank=rank,name=name,count=count,ratin=ratin,
    rank1=rank1,name1=name1,countr=countr,rating=rating)
    



app.run(debug=True)    