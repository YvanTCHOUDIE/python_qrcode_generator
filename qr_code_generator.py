import qrcode
#import sqlite3
#import cx_Oracle
#import pyodbc 
import numpy as np
import pandas as pd
import pandas.io.sql as pd_sql
from datetime import date
from datetime import datetime
from datetime import timedelta
#from sqlalchemy.engine import create_engine
#from sqlalchemy.exc import SQLAlchemyError
from IPython.display import display


df_data = pd.read_csv('./inp_file/data.csv');

for index, client_row in df_data.iterrows():
    print(client_row['client_name']);
    name = client_row['client_name'];
    data = "https://my_website.com/clients/?name={}".format(name.replace(" ", "___---"));

    img = qrcode.make(data);

    img.save("./outputs/{}_qrcode.png".format(name));

