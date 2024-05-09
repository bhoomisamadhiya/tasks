# script that reads data row by row from excel sheet and uploads to a database.

import pandas as pd
from sqlalchemy import create_engine

def data_read_insert(excl, db_url, table):
    
    #reads the excel file 
    read = pd.read_excel(excl)
    print(read.head())

    #creates a db connection engine
    engine = create_engine(db_url)


    #to insert the contents of the DataFrame read into the specified table (table) in the database represented by the SQLAlchemy engine engine.
    # If the table already exists, it will append the data to the existing table, and the DataFrame index will not be included in the inserted data.
    read['OrderDate'] = pd.to_datetime(read['OrderDate']).dt.strftime('%d-%m-%y')
    read.to_sql(table, con=engine, if_exists='append', index=False)


if __name__ == "__main__":
    excl = "/home/my/Documents/data_insert.xlsx"
    db_url = "mysql://test:testlocal@localhost:3306/test"   #CREATE USER 'test'@'localhost' IDENTIFIED BY 'testlocal';
    table = "test_insert"

    data_read_insert(excl, db_url, table)
