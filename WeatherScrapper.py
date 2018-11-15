# -*- coding: ISO-8859-1 -*-
import requests
import bs4
import time
from datetime import datetime as DateTime, timedelta as TimeDelta
from gtts import gTTS
import os
guardaChuva = 0
casaco = 0
chuva = 0
casacotemp = 0
casacovent = 0
    
def calcRecom():
    global hora
    global x
    global a
    global temp
    global h_inicio
    global guardaChuva
    global casacotemp
    global casacovent
    global chuva
    hora = 0
    x=62
    while(x<436):  
        if hora=="23":
            
            x=450
        else:
            #Pesquisar Hora
            a = hi[x].getText()
            if a == "12:00 am":
                a = "00"
            elif a == "1:00 am":
                a = "01"
            elif a == "2:00 am":
                a = "02"
            elif a == "3:00 am":
                a = "03"
            elif a == "4:00 am":
                a = "04"
            elif a == "5:00 am":
                a = "05"
            elif a == "6:00 am":
                a = "06"
            elif a == "7:00 am":
                a = "07"
            elif a == "8:00 am":
                a = "08"
            elif a == "9:00 am":
                a = "09"
            elif a == "10:00 am":
                a = "10"
            elif a == "11:00 am":
                a = "11"
            elif a == "12:00 pm":
                a = "12" 
            elif a == "1:00 pm":
                a = "13"
            elif a == "2:00 pm":
                a = "14"
            elif a == "3:00 pm":
                a = "15"
            elif a == "4:00 pm":
                a = "16"
            elif a == "5:00 pm":
                a = "17"
            elif a == "6:00 pm":
                a = "18"
            elif a == "7:00 pm":
                a = "19"
            elif a == "8:00 pm":
                a = "20"
            elif a == "9:00 pm":
                a = "21"
            elif a == "10:00 pm":
                a = "22"
            elif a == "11:00 pm":
                a = "23"
            else:
                a = a[:-3]
            #print("Hora                     " + a)
            hora = a

            #Pesquisar Temperatura
            a = hi[x+6].getText()
            a = a[:-3]
            a = (int(a) - 32)*5/9
            #print("Temperatura              " + str(a))
            temp = a

        
            #Pesquisar probabilidade de chuva
            a = hi[x+7].getText()
            a = a[:-1]
            print a
            chuva = int(a)
            #print("Tamanho da precipitaçao " + str(a))
            

            #Pesquisar vento
            a = hi[x+12].getText()
            a = a[:2]
            a = round((int(a) * 1.60934),2)
            #print("Força do vento          " + str(a))
            vento = a

            #print("  ")

            #file.write(str(hora) + ";" + str(temp) + ";" + str(chuva) + str(vento) +"\n")
            #print hora
            #print h_inicio
            if int(hora) == int(h_inicio):
                file.write(str(hora) + " horas vai estar uma temperatura de " + str(temp) + "graus centigrados e uma chuva com uma grossura de " + str(chuva) + ", e um vento de intensidade " + str(vento) +" kilometros por hora\n")

                #CONDIÇÕES DAS RECOMENDAÇÕES
                if chuva > 10:
                    guardaChuva = 1
                if temp < 20:
                    casacotemp = 1
                if vento > 10:
                    casacovent = 1
                h_inicio = h_inicio+1
                if int(hora) == int(h_fim):
                    h_inicio = h_inicio-1
            x=x+16    
    print("  ")
    print ('RECOMENDAÇÕES')
    if casacotemp == 1:
        text = "Recomenda-se o uso de casaco devido ás temperaturas baixas"
        #tts = gTTS(text, lang='pt-PT')
        print (text)
        file.write(text)
        #tts.save("Recomendacoes1.mp3")
        #os.system("Recomendacoes1.mp3")
        time.sleep(4)
    if casacovent == 1:
        text = "Recomenda-se o uso de casaco devido ao vento forte"
        #tts = gTTS(text, lang='pt-PT')
        print (text)
        file.write(text)
        #tts.save("Recomendacoes1.mp3")
        #os.system("Recomendacoes1.mp3")
    if guardaChuva == 1:
        text = "Recomenda-se o uso de guarda chuva"
        #tts = gTTS(text, lang='pt-PT')
        print(text)
        file.write(text)
        #tts.save("Recomendacoes2.mp3")
        #os.system("Recomendacoes2.mp3")
        time.sleep(4)
    if casacotemp == 0 and casacovent == 0:
        text = "Recomenda-se o uso de roupas frescas"
        #tts = gTTS(text, lang='pt-PT')
        print(text)
        file.write(text + "\n")
        #tts.save("Recomendacoes3.mp3")
        #os.system("Recomendacoes3.mp3")
        time.sleep(4)
    file.close()

#-----------------------------------------------------------------MAIN-----------------------------------------------------------------------------
op = input("A que dia deseja obter a sua previsão? Hoje(1)/Amanha(2) ")
if op == 1:
    opp = input("Deseja sabes durante o dia todo ou parte? Inteiro(1)/Parte(2) ")
    if opp == 1:    
        h_inicio = int(DateTime.today().strftime("%H"))+1
        h_fim = 23
    else: 
        h_inicio = input("A partir de que hora? ")
        h_fim = input("Até que hora? ")
    
#------------------------------------------------------Pesquisar Tempo para o dia de hoje----------------------------------------------------------
    date = DateTime.today().strftime("%Y-%m-%d")
    print 'Tempo para o dia de ' + str(date)
    link = 'https://www.wunderground.com/hourly/us/ca/san-francisco/37.78%2C-122.40?cm_ven=localwx_hour'
    print link
    #Scrap Info   
    res = requests.get(link)
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    type(soup)
    hi = soup.select("span")

    #Open File
    file = open("tempoHoje.txt","w")

    #Get Data
    hoje = DateTime.today() 
    date = hoje.strftime("%Y-%m-%d")
    file.write('-----------------------Tempo para o dia de ' + str(date) + '-----------------------\n')
    print('')
    calcRecom()

#-----------------------------------------------------------------Pesquisar Tempo para o dia de amanha-----------------------------------------------------------------------------  
else:
    opp = input("Deseja sabes durante o dia todo ou parte? Inteiro(1)/Parte(2) ")
    if opp == 1:
        h_inicio = 01
        h_fim = 23
    else: 
        h_inicio = input("A partir de que hora? ")
        h_fim = input("Até que hora? ")

        
    #Pesquisar Tempo para amanha
    hoje = DateTime.today() 
    amanha = hoje + TimeDelta(days=1)
    date = amanha.strftime("%Y-%m-%d")
    
    print 'Tempo para o dia de ' + str(date)
    
    link = 'https://www.wunderground.com/hourly/pt/san-francisco/date/'+date+'?cm_ven=localwx_hour'

    #Scrap Info
    res = requests.get(link)
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    type(soup)
    hi = soup.select("span")

    #Open File
    file = open("tempoAmanha.txt","w")   
    file.write('-----------------------Tempo para o dia de ' + str(date) + '-----------------------\n')
    print('')
    calcRecom()
print("Scrap Done")

