from facebook_scraper import get_posts
import pandas as pd

posts = get_posts('write facebook page name', pages=60, extra_info=True)
post_date_arr = []
likes_arr = []
comments_arr = []
shares_arr = []
url_arr = []
post_text_arr = []

for post in posts:
    post_date_arr += [post['time']]
    likes_arr += [post['likes']]
    comments_arr += [post['comments']]
    shares_arr += [post['shares']]
    url_arr += [post['post_url']]
    post_text_arr += [post['post_text']]

df = pd.DataFrame({'Date':post_date_arr,'Post': post_text_arr,'Link':url_arr,'Likes':likes_arr,'Comments':comments_arr,'Shares':shares_arr})
df.to_csv('out.csv')


    
"""from facebook_scraper import get_posts

credentials = ('write your facebook username','write your facebook password')
posts = get_posts('CAD.MASTERS', pages=10, extra_info=True,credentials = credentials)
for post in posts:
    print('Posted at: ', post['time'])
    print('number of likes: ',post["likes"] )
    print( "number of shares: " , post["shares"])
    print( "number of comments: " , post["comments"])
    print("'''''''",post["post_url"],"''''''")
    print(post["post_text"])"""
    
    















    
