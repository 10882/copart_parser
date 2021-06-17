import bs4
from selenium import webdriver
from time import sleep



def monitor(link):

    data = {
        'user_agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.396'
    }

    browser = webdriver.Chrome('cd.exe')

    browser.get(link)

    sleep(7.0)

    code = browser.page_source

    code = bytes(code, encoding= 'Utf-8')

    browser.quit()


    soup = bs4.BeautifulSoup(code, features="lxml")

    soup = soup.find(class_ = 'inner-wrap d-f-c f-1')

    soup = soup.find(class_ = 'main-content d-f-c f-1')

    soup = soup.find(class_ = 'lot-details-page bg-gray')

    soup = soup.find(class_ = 'container-fluid lot-details-description')

    soup = soup.find(class_ = 'col-lg-3 col-md-4 col-xs-12 right bid-information pr-0')

    soup = soup.find(class_ = 'col-md-12 col-xs-12')

    soup = soup.find(class_ = 'lot-details-inner')
    
    soup = soup.find(class_ = 'panel-content clearfix ng-pristine ng-valid ng-valid-maxlength')


    try:
        soupn = soup.findAll(class_ = 'border-top-gray pt-5 clearfix')


        soupn = soupn[1].find(class_ = 'bid-price')

        for i in soupn:
            if i != '':
                return(i[6:-5])

    except: 
        soup = soup.findAll(class_ = 'border-top-gray')

        soup = soup[2]

        soup = soup.find(class_ = 'pt-5 clearfix')
        soup = soup.find(class_ = 'text-right bid-price')
        for i in soup:
            if i != '':
                return(i[6:-5])       
