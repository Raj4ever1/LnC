import enum
import json
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseQueryStringSelect(enum.Enum):
    OPTIONS_USING_USER_ID = 'select DISTINCT(o.[option]), Concat(o.role_id,o.id) as "function_key"  from [options_option] as o,authentication_user as u, authentication_userrolemap as ur where o.role_id = ur.role_id_id and ur.user_id_id = {} ORDER BY o.[option]'
    OPTIONS_USING_ROLE_ID = 'select DISTINCT(o.[option]), Concat(o.role_id,o.id) as "function_key"  from [options_option] as o,authentication_user as u, authentication_userrolemap as ur where o.role_id = {} ORDER BY o.[option]'
    TOKEN_USING_USER = "select a.[key] FROM authtoken_token as a, authentication_user as u where a.user_id = u.id and u.email = '{}'"
    ROLES_USING_USER_ID = 'select role_id_id from authentication_userrolemap where user_id_id = {}'
    ALL_EVENTS = 'select id from event_event'
    EVENT_USING_EVENT_ID = 'select * from event_event as e where e.id = {}'
    LIST_OF_MANAGERS = 'SELECT user_id_id from authentication_userrolemap where role_id_id = 2'
    GAMES_USING_EVENT_ID= 'SELECT g.name,g.description,g.no_of_players,egm.start_date,egm.end_date,egm.max_players,egm.min_players,egm.game_id_id FROM event_eventgamemap as egm, game_game as g where g.id = egm.game_id_id and egm.event_id_id = {}'
    MANAGERS_FOR_EVENT = 'select DISTINCT(user_id_id) from event_eventusermap where event_id_id = {}'
    
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
            resultElement= dict(sorted(resultElement.items()))
            resultList.append(resultElement)
        return resultList
    
    def insert(self, table_name, data:dict):
        insert_string = 'insert into {} ({}) VALUES {};'
        print(insert_string.format(table_name, ', '.join(tuple(data.keys())), tuple(data.values())))
        self.cursor.execute(insert_string.format(table_name, ', '.join(tuple(data.keys())), tuple(data.values())))
        self.cursor.commit()
        resultElement = {}
        for i in self.cursor.execute('select * from {}'.format(table_name)).fetchall()[-1:]:
            for j in range(len(i)):
                resultElement[i.cursor_description[j][0]] = i[j]
        return resultElement