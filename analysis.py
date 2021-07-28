import matplotlib.pyplot as plt
from scrape import Scrape


# class Charts(Scrape):
class Charts:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def see_charts(self):
        # this plots the bar chart
        plt.bar(self.x, self.y, width=0.4, color="red")
        plt.show()

        # this plots the pie chart
        plt.pie(self.y, labels=self.x, shadow=True, autopct='%1.0f%%')
        plt.show()

# chart = Charts()
