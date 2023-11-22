class AccessDeniedError(Exception):
    def __init__(self,data):
        print(data)
        super().__init__("hello wordl",data)

class UnableToAddContactError(Exception):
    def __init__(self,data):
        print(data)
        super().__init__("Unable to add contact in Bitrix24")

class UnableToUpdateContactError(Exception):
    def __init__(self,data):
        print(data)
        super().__init__("Unable to update contact in Bitrix24")