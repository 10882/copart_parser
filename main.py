from gui.Gui import *
from core.copart import *

def main():
    hello()
    link = select()
    oldp = ''
    while True:
        price = monitor(link)
        if oldp != price:
            print(price)
            oldp = price
        sleep(60.0)


if __name__ == '__main__':
    main()