import enum
import json
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseQueryStringSelect(enum.Enum):
    OPTIONS_USING_USER_ID = 'select DISTINCT(o.[option]), Concat(o.role_id,o.id) as "function_key"  from [options_option] as o,authentication_user as u, authentication_userrolemap as ur where o.role_id = ur.role_id_id and ur.user_id_id = {} ORDER BY o.[option]'
    OPTIONS_USING_ROLE_ID = 'select DISTINCT(o.[option]), Concat(o.role_id,o.id) as "function_key"  from [options_option] as o,authentication_user as u, authentication_userrolemap as ur where o.role_id = {} ORDER BY o.[option]'
    USER_USING_TOKEN = 'select user_id  FROM authtoken_token where key = {}'
    ROLES_USING_USER_ID = 'select role_id_id from authentication_userrolemap where user_id_id = {}'
    
class DatabaseQuery():
    def __init__(self):
        server = 'localhost' 
        database = 'LearnAndCode'#database
        username = 'ronak1' 
        password = os.getenv('Database_password') 
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};Trusted_Connection=yes;SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
        self.cursor = cnxn.cursor()
        
    def select(self, query:DatabaseQueryStringSelect, args=None):
        result = None
        if not args:
            result = self.cursor.execute(query.value).fetchall()
        else:
            result = self.cursor.execute(query.value.format(args)).fetchall()
        resultList = []
        for i in result:
            resultElement = {}
            for j in range(len(i)):
                resultElement[i.cursor_description[j][0]] = i[j]
            resultList.append(resultElement)
        return resultList