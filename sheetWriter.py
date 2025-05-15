import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

sheetId = 'insira-o-id-da-sua-planilha-aqui';
googleDocsAcessKey = 'chave-de-acesso-ao-docs.json';

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning);
SCOPE = ['https://www.googleapis.com/auth/spreadsheets'];
credentials = Credentials.from_service_account_file(googleDocsAcessKey, scopes=SCOPE);
service = build('sheets', 'v4', credentials=credentials);

def parse(url): 
    res = requests.get(url);
    soup = BeautifulSoup(res.text, 'html.parser');
    names = soup.find_all('span', class_='txtTit');
    prices = soup.find_all('span', class_='valor');
    return zip(names, prices);

def read(path):
    f = open(path);
    value = f.read();
    f.close();
    return value;

def writeRange(range):
    f = open("range.txt", "w");
    value = f.write(range);
    f.close();

def writeToSheet(url):
    sheet = service.spreadsheets();
    values = [];
    for name, value in parse(url):
        values.append([name.text.strip(), value.text.strip()]);
    body = {'values': values};
    range = read("range.txt");
    write = sheet.values().update(spreadsheetId=sheetId, range=f"A{range}", valueInputOption='RAW', body=body).execute();
    writeRange(str(len(values) + int(range)))


if __name__ == "__main__":
    bills = read("notas.txt").split();
    for bill in bills:
        writeToSheet(bill);