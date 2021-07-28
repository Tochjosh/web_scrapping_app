# Entry point of your application
from analysis import Charts
from scrape import Scrape


def main():
    while True:  # Validation of the entered value is done here
        query = input("Would you like to scrape a website (y/n)? ")
        if query.lower() in ['y', 'n']:
            break
        else:
            print("Enter 'y' or 'n'")
    if query == 'y':
        scrapper.check_url()  # checks the website url
        top_word = scrapper.scrape_website()  # calls the scrapper
        chart_maker = Charts(top_word.keys(), top_word.values())  # stores the keys and values in separate lists
        chart_maker.see_charts()  # chart is generated here
        main()  # calls the prompt all over again
    else:
        print("Thank you for analyzing, come back again")
        exit()


scrapper = Scrape()

if __name__ == '__main__':
    main()
