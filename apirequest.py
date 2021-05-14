# import requests,json,os 
# if os.path.exists('courses.json'):
# 	file = open("courses.json")
# 	temp = file.read()
# 	data = json.loads(temp)
# 	file.close()
# else:
# 	request = requests.get("http://saral.navgurukul.org/api/courses")
# 	data = request.json()
# 	s = json.dumps(data)
# 	with open("courses.json", "w") as file:
# 		file.write(s)
# 		file.close()

# list_of_id = []
# for i in range(len(data["availableCourses"])):
# 	print(i+1,':',data["availableCourses"][i]["name"])
# 	list_of_id.append(data["availableCourses"][i]["id"])
# print()
# choice=int(input("Which course you want to join  "))
# print()                                 
# for i in range(len(list_of_id)):
#     if (choice-1) == i:
#         course_name = data['availableCourses'][i]["name"]
#         request1=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_of_id[i])+"/exercises")
#         subdata=request1.json()

# parent = subdata["data"]
# f=1
# a={}
# for i in range(len(parent)):
#     print(f'{str(f)} :{parent[i]["name"]}')
#     a[str(f)]=parent[i]["slug"]
#     c=1
#     for j in range(len(parent[i]['childExercises'])):
#         z=str(f)+'.'+str(c)
#         a[z]=parent[i]['childExercises'][j]["slug"]
#         print("  ",z,parent[i]['childExercises'][j]["name"])
#         c+=1
#     f+=1
# print()
# user_input=input("Enter which slug you want to see  ")
# print()
# for i in a:
#     if user_input == i:
#         request2 = requests.get("http://saral.navgurukul.org/api/String(i)"+"."+"String(c)courses/12/exercise/getBySlug?slug="+str(a[i]))
#         sc = request2.json()
#         print(sc['content'])
#         break

from bs4 import BeautifulSoup
import requests
import json
from  pprint import pprint

def scrap_top_list():
    url ="https://www.imdb.com/india/top-rated-indian-movies/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"html.parser")
    data = soup.find("tbody",class_="lister-list").findAll("tr")
    movies , rateing , years , position ,links= [],[],[],[],[]
    for movie in data:
        movies.append(movie.find("td",class_="titleColumn").find("a").get_text())
        rate = (movie.find("td",class_="ratingColumn imdbRating").text)
        rateing.append(float(rate.strip()))
        years.append(int(movie.find("span",class_="secondaryInfo").text[1:5]))
        position.append(int(movie.text.strip().split('.')[0]))
        links.append('https://www.imdb.com'+movie.find('a').get('href'))
    return page_info(movies,rateing,years,position,links)
def page_info(movies,rateing,years,position,links):
    d={}
    top_250_movieas = []
    for i,j,k,l,m in zip(movies,rateing,links,years,position):
        d['name'] = i
        d['rating'] = j
        d['links'] = k
        d['years'] = l
        d['postion'] = m
        top_250_movieas.append(d.copy())
    f=open('data_aagya.json','w')
    json.dump(top_250_movieas,f,indent=4)
    f.close()
    return top_250_movieas
pprint((scrap_top_list()))