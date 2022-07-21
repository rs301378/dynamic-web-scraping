#Dyanmix website scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd 

url = "https://www.youtube.com/channel/UCB8COLBcStcSp_wyXvTQl9Q/videos?view=0&sort=p&flow=grid"

driver = webdriver.Chrome('/home/awadh/Test-folder/scraping/chromedriver')
driver.get(url)

videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-grid-video-renderer')

videos_list = []

for video in videos:
    title = video.find_element(By.XPATH,'.//*[@id="video-title"]').text
    view = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text

    #print(title, view, when)

    vid_item = {
        'title' : title,
        'views' : view,
        'posted' : when
    }
    videos_list.append(vid_item)

df = pd.DataFrame(videos_list)
print(df)


