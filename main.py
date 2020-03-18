#Imports
import numpy as np
import requests

#Init
DATABASE = [
    ["1-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-01-2020.csv"],
    ["2-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-02-2020.csv"],
    ["3-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-03-2020.csv"],
    ["4-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-04-2020.csv"],
    ["5-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-05-2020.csv"],
    ["6-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-06-2020.csv"],
    ["7-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-07-2020.csv"],
    ["8-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-08-2020.csv"],
    ["9-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-09-2020.csv"],
    ["10-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-10-2020.csv"],
    ["11-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-11-2020.csv"],
    ["12-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-12-2020.csv"],
    ["13-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-13-2020.csv"],
    ["14-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-14-2020.csv"],
    ["15-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-15-2020.csv"],
    ["16-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-16-2020.csv"],
    ["17-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"]
]
#DATA_SITE  = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"

#Main
if __name__ == "__main__":
    #Aquiring and organizing data
    DB = []
    for DATA_SITE in DATABASE:
        r = requests.get(DATA_SITE[1])
        dataString = r.text
        dataList = dataString.split("\n")
        dataKeys = dataList[0].split(",")
        dataSheet = []
        for country in dataList[1:]:
            dataSheet.append(country.split(","))
        parcel = (DATA_SITE[0], dataSheet)
        DB.append(parcel)

print("Done") #Line to enable breakpoints for debug purposes