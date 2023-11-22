import requests
import json
from utils.utils import *
from utils.Errors import *
from config import *

def get_data_from_db():
    con,cur = db_connection()
    sql= "SELECT * FROM userdata"
    cur.execute(sql)
    return cursor_to_list(cur)

def Api_to_get_all_Phonenumber():
    Api = requests.post(f"{url}/crm.contact.list.json",json=list_select,headers = header)
    if Api.status_code == 200:
        return [int(i['ID']) for i in Api.json()['result']];
    raise AccessDeniedError("Can able to access the contact ")

def add_to_contact_list(data):
    data = data_conversion(data)
    Api = requests.post(f"{url}/crm.contact.add.json",data=json.dumps(data,default=str),headers = header)
    if Api.status_code == 200:
        print("Add to contact list")
    else:
        raise UnableToAddContactError()

def update_contact_list(data):
    data = data_conversion(data)
    Api = requests.post(f"{url}/crm.contact.update.json?id={data['fields']['ID']}",data=json.dumps(data,default=str),headers = header)
    if Api.status_code == 200:
        print("updated to contact list")
    else:
        raise UnableToUpdateContactError()

def main():
    db_data = get_data_from_db()
    all_Users_id = Api_to_get_all_Phonenumber()
    print(all_Users_id)
    for data in db_data:
        if data["id"] in all_Users_id:
            update_contact_list(data)
        else:
            add_to_contact_list(data)

if __name__ == '__main__':
    main()
