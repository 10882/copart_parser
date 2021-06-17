import os
from time import sleep
from selenium import webdriver

global zast 

zast = '''
   m    #             mmm     mmmm   mmmm   mmmm   mmmm 
 mm#mm  # mm    mmm     #    m"  "m #    # #    # "   "#
   #    #"  #  #"  #    #    #  m # "mmmm" "mmmm"     m"
   #    #   #  #""""    #    #    # #   "# #   "#   m"  
   "mm  #   #  "#mm"  mm#mm   #mm#  "#mmm" "#mmm" m#mmmm
                                                        
'''


def hello():
    print(zast)
    sleep(4)
    os.system('cls')

def select():

    driver = webdriver.Chrome('cd.exe')
    
    driver.get('https://www.copart.com')

    input("Press any key, when you select page")

    link = driver.current_url

    driver.quit()

    return(link)
