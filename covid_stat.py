import time
from covid.data_it import get_and_process_covid_data_it
import schedule
import requests
import telepot
import csv
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import time
import pandas as pd
import numpy as np

# Dataset
from covid.data import get_data
# Models
from covid.models.bettencourt_ribeiro import bettencourt_ribeiro
idx = pd.IndexSlice

data=get_and_process_covid_data_it(pd.Timestamp.today())

days= data.loc[idx["Italia"]].index
cases = data.loc[idx["Italia"], "positive"]

fig,ax1 = plt.subplots()


ax1.plot(days, cases,'o', markersize=1, label="Casi Covid Italia")
plt.legend(loc="upper left")
plt.xlabel('Giorni')
plt.xticks(rotation=45)
plt.ylabel('Casi Giornalieri')
plt.grid(axis="y",linestyle='-', linewidth=1)
plt.savefig('/home/fabio/CovidAnalysisBot/Grafici/casi.png', dpi=399)
#plt.show()

#Telegram
def report():
    bot = telepot.Bot('5023870649:AAGSGZaOQMzkGx43o1G0yP888-iDN-vzut0')
    bot.sendPhoto(405229696, photo=open('/home/fabio/CovidAnalysisBot/Grafici/casi.png', 'rb'))
    #bot.sendDocument(405229696, document=open('Covid/casi.pdf', 'rb'))
    new_cases = cases[len(cases)-1];
    bot.sendMessage(405229696, "Ci sono " + str(new_cases) + " nuovi casi di Covid-19")

    bot.sendPhoto(405229696, photo=open('/home/fabio/CovidAnalysisBot/Grafici/Rt.png', 'rb'))
    


report()
#schedule.every().day.at("17:01").do(report)
#while True:
#    schedule.run_pending()
#    time.sleep(1)



