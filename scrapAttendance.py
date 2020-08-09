from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import csv
import time
import json
import sys


class ScrapAttendance:
      def __init__(self):
        snapshot = 0
        chrome_path = r"C:\Users\ShalomAlexander\Downloads\chromedriver_win32\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
        print("Fetching....1")   
        attendance = dict() 
        while True:
          print("Fetching....2")
          snapshot += 1
          student_name_element_xpath = '//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[1]/div[2]'                            
          posts = driver.find_elements_by_xpath(student_name_element_xpath)
          posts = (posts[0].text).split("\n")
          #now_time = datetime.datetime.now()
          for post in posts:
               if post not in attendance.keys(): 
                    attendance[post] = 1
               else:
                    attendance[post] += 1

          attendance["snapshot"] = snapshot

          print("Updating result.json....")
          for key, value in  attendance.items():
               with open('result.json', 'w') as fp:
                    json.dump(attendance, fp)          
          
          time.sleep(2)


                 

if __name__ == '__main__':
     print("Main function")
     scrap_attendance = ScrapAttendance()


