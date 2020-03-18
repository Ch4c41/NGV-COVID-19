#Imports
import numpy as np
import requests

#Init
DATA_SITE  = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"



#Main




if __name__ == "__main__":
    r = requests.get(DATA_SITE)
    print(r.text)