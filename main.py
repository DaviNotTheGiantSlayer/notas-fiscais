import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning);
chaveDeAcessoGoogleDocs = 'optimal-cabinet-291113-95cb845ead5c.json';
ESCOPO = ['https://www.googleapis.com/auth/spreadsheets'];
credenciais = Credentials.from_service_account_file(chaveDeAcessoGoogleDocs, scopes=ESCOPO);
servico = build('sheets', 'v4', credentials=credenciais);
idPlanilha = '1RRj1-Qrd3RFoLl8RDfIA8_Q_GYTomjO3mrMTDpvTqCg';    

def parse(url):
    res = requests.get(url);
    soup = BeautifulSoup(res.text, 'html.parser');
    nomes = soup.find_all('span', class_='txtTit');
    precos = soup.find_all('span', class_='valor');
    return zip(nomes, precos);

def readRange():
    f = open("range.txt");
    value = f.read();
    f.close();
    return value

def writeRange(range):
    f = open("range.txt", "w");
    value = f.write(range);
    f.close();

def writeToSheet(url):
    planilha = servico.spreadsheets();
    valores = [];
    for nome, valor in parse(url):
        valores.append([nome.text.strip(), valor.text.strip()]);
    corpo = {'values': valores};
    range = readRange();
    escrever = planilha.values().update(spreadsheetId=idPlanilha, range=f"A{range}", valueInputOption='RAW', body=corpo).execute();
    writeRange(str(len(valores) + int(range)))


if __name__ == "__main__":
    writeToSheet('https://www.dfe.ms.gov.br/nfce/qrcode/?p=50250479379491005495651150001523661901823811%7C2%7C1%7C1%7C09A914C4536DC289657B06B93B46B7C2ADB3F711');