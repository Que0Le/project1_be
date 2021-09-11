from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.db.events import close_db_connection, connect_to_db

from app.core.config import settings
from O365 import Account, MSGraphProtocol

CLIENT_ID = '3a9eef7d-ab34-45f1-a9fd-3780564d7a2e'
SECRET_ID = '<your secret id>'
SECRET_VALUE = 'kpiQvG6_4ovz05n4c7Sn8.KOZE0rT.21s_'

credentials = (CLIENT_ID, SECRET_VALUE)
scopes = [
   'https://graph.microsoft.com/Mail.ReadWrite', 
   'https://graph.microsoft.com/Mail.Send',
   'https://graph.microsoft.com/Calendars.ReadWrite',
   'offline_access'
]

def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        await connect_to_db(app)
    
    protocol = MSGraphProtocol() 
    account = Account(credentials, protocol=protocol)
    if account.authenticate(scopes=scopes):
        print('Authenticated!')
        settings.account = account
    else:
        print("Auth O365 failed!")

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app

""" 
import datetime as dt
from O365 import Account, MSGraphProtocol

CLIENT_ID = '3a9eef7d-ab34-45f1-a9fd-3780564d7a2e'
SECRET_ID = '<your secret id>'
SECRET_VALUE = 'kpiQvG6_4ovz05n4c7Sn8.KOZE0rT.21s_'

credentials = (CLIENT_ID, SECRET_VALUE)



scopes = [
   'https://graph.microsoft.com/Mail.ReadWrite', 
   'https://graph.microsoft.com/Mail.Send',
   'https://graph.microsoft.com/Calendars.ReadWrite'
]

# account = Account(credentials, scopes=scopes)
# account.authenticate()

protocol = MSGraphProtocol() 
# #protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>') 
# scopes = ['Calendars.Read.Shared']
account = Account(credentials, protocol=protocol)

if account.authenticate(scopes=scopes):
   print('Authenticated!')
"""