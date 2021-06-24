
# import facebook

# api = API(app_id="279807803755087", app_secret="474a426272b9c5533df07e36f9c51486", application_only_auth=True)
# api.get_token_info()
# AccessToken(app_id='279807803755087', application='ggg', user_id=None)


# api.get_page_info(username='akinkunmi ng')
# Page(id='279807803755087', name='Facebook', username='akinkunmi ng')


# import facebook

# import urllib3

# import requests

# # def request(self, path, args=None, post_args=None, files=None, method=None)

# token = '279807803755087|zRWYG5_WjwLZgfncJpFxIozXsFA'

# graph = facebook.GraphAPI(access_token=token, version=8.0)
# posts = graph.search(q="nasiru", type="post")

# print (posts['data'])

# graph = facebook.GraphAPI(token)
# data = graph.request('/search?q=nasiru&type=user')
# print (data)


# import mechanize
# import re
# import csv

# user_info = []

# fb_url = 'http://www.facebook.com/100004210542493'
# br = mechanize.Browser()
# br.set_handle_robots(False)

# br.open(fb_url)
# all_html = br.response().get_data()
# print (all_html)

# city = bytes(re.search('fsl fwb fcb">(.+?)</a></div><div class="aboutSubtitle fsm fwn fcg', all_html).group(1))

# user_info = [fb_url, city]
# print (user_info)

from urllib.request import urlopen
from bs4 import BeautifulSoup

#url = input("enter url: ")

try:
   page = urlopen("https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/#:~:text=Beautiful%20Soup%20also%20relies%20on,and%20attempt%20to%20import%20lxml).")
except:
   print("Error opening the URL")

soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify().encode('utf-8'))
content = soup.find('div', {"class": "container"})

friends = ''
for i in content.findAll('a'):
    friends = friends + ' ' +  i.text

print(friends)

# import facebook

# page_token = '279807803755087|zRWYG5_WjwLZgfncJpFxIozXsFA'
# graph = facebook.GraphAPI(access_token=page_token, version="3.1")

# default_info = graph.get_object(id='https://www.facebook.com/gbolahan.akinkunmi.3')

# print(default_info)

# from fb import API
# fbapi = API("279807803755087","474a426272b9c5533df07e36f9c51486")
# friends = fbapi.using(user_access_token).me.friends.get()


#this program is simply used to learn scrapping facebook properly
# from urllib.request import urlopen
# import json
# import datetime
# import csv
# import sys

# def create_comments_url(graph_url,post_id, APP_ID, APP_SECRET):
#     comments_args = post_id + "/comments/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
#     comments_url = graph_url + comments_args
#     return comments_url

# # defined function that creates post_url
# def create_post_url(graph_url, APP_ID, APP_SECRET):
#     post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
#     post_url = graph_url + post_args
#     return post_url

# #defined function that converts page data in json form
# def take_data_to_json(graph_url):
#     web_response = urlopen(graph_url)
#     readable_page = web_response.read().decode('utf-8')
#     json_data = json.loads(readable_page)

#     return json_data

# #this function used search specified time interval
# def scrap_post_by_date(graph_url, date, post_data):

#     page_posts = take_data_to_json(graph_url)

#     next_page = page_posts["paging"]["next"]

#     page_posts = page_posts["data"]

#     collecting = True

#     for post in page_posts:
#         try:
#             current_posts = [post["created_time"],post["id"]]
#         except Exception:
#             current_posts = ["error","error","error"]
#         if current_posts[0] != "error":

#             if date <= current_posts[0]:
#                 post_data.append(current_posts[1])
#             elif date > current_posts[0]:
#                 print ("Done collecting")
#                 collecting = False
#                 break

#     if collecting == True:
        
#         scrap_post_by_date(next_page,date,post_data)
#     return post_data


# def get_comments_data(comment_url,comment_data):

#     comments = take_data_to_json(comment_url)["data"]


#     for comment in comments:
#         try:
#             current_comment = [comment["id"],comment["message"],comment["from"]["name"]]
#             comment_data.append(current_comment)


#         except Exception:
#             current_comment = ["error","error","error"]


#     try:
        
#         next_page = take_data_to_json(comment_url)["paging"]["next"]
#     except Exception:
#         next_page = None


#     if next_page is not None:
#         get_comments_data(next_page,comment_data)
#     else:
#         return comment_data



# def main():
#     App_SECRET = sys.argv[3]
#     APP_ID = sys.argv[4]
#     userName = sys.argv[1]
    

#     last_crawl = datetime.datetime.now() - datetime.timedelta(int(sys.argv[2]))
#     last_crawl = last_crawl.isoformat()

#     list_papers = [userName]

#     graph_url = "https://graph.facebook.com/"

#     outputFile = open('outFile.csv','w',newline="",encoding='utf-16')
#     outputWriter = csv.writer(outputFile,delimiter = '\t')




#     for paper in list_papers:
#         current_page = graph_url + paper

#         #json_fbpage = take_data_to_json(current_page)

#         post_url = create_post_url(current_page, APP_ID, App_SECRET)


#         post_data = []

#         post_data = scrap_post_by_date(post_url,last_crawl,post_data)







#     #this for loop post_data contains post_id's



#     for post in post_data:
#         comment_url_full = create_comments_url(graph_url,post,APP_ID,App_SECRET)
#         #getting data in json format
#         comment_collected = []

#         get_comments_data(comment_url_full,comment_collected)




        

#         for comment in comment_collected:

            



#             outputWriter.writerow([post,comment[0],comment[2],comment[1]])
#     outputFile.close()


# if __name__ == '__main__':
#     main()
