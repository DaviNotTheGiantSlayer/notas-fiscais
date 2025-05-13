import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning);
googleDocsAcessKey = 'chave-de-acesso-ao-docs.json';
SCOPE = ['https://www.googleapis.com/auth/spreadsheets'];
credentials = Credentials.from_service_account_file(googleDocsAcessKey, scopes=SCOPE);
service = build('sheets', 'v4', credentials=credentials);
sheetId = 'insira-o-id-da-sua-planilha-aqui';    

def parse(url): 
    res = requests.get(url);
    soup = BeautifulSoup(res.text, 'html.parser');
    names = soup.find_all('span', class_='txtTit');
    prices = soup.find_all('span', class_='valor');
    return zip(names, prices;

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
    sheet = service.spreadsheets();
    values = [];
    for name, value in parse(url):
        values.append([name.text.strip(), value.text.strip()]);
    body = {'values': valores};
    range = readRange();
    write = planilha.values().update(spreadsheetId=sheetId, range=f"A{range}", valueInputOption='RAW', body=body).execute();
    writeRange(str(len(values) + int(range)))


if __name__ == "__main__":
    writeToSheet('https://www.dfe.ms.gov.br/nfce/qrcode/?p=50250479379491005495651150001523661901823811%7C2%7C1%7C1%7C09A914C4536DC289657B06B93B46B7C2ADB3F711');