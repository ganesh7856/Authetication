import requests

TOKEN_URI = "http://localhost:8000/token/"

EMP_BASE_URI = "http://localhost:8000/emp/api/v1/"



APP_TOKEN_GUEST_AMIT = 'Token f3e2fa2f018ed68306764946b13043c0cdc96f60'
APP_TOKEN_AD1_SUNNY = 'Token f3e2fa2f018ed68306764946b13043c0cdc96f60'
APP_TOKEN_SUPERUSER_GANESH = 'Token 99851c4f42c628a3a691dec25d6fbad80acbdc41'


dict_token_val1 = {'Authorization' : APP_TOKEN_GUEST_AMIT}
dict_token_val2 = {'Authorization' : APP_TOKEN_AD1_SUNNY}
dict_token_val3 = {'Authorization' : APP_TOKEN_SUPERUSER_GANESH}



def get_token_for_user(user,pwd):
    response = requests.post(TOKEN_URI,json={"username":user,"password":pwd})
    #response = requests.post(TOKEN_URI,user,pwd)
    print(response.status_code)
    print(response.json())
    return response.json()

def get_all_emps_without_token():
    response = requests.get(EMP_BASE_URI) #guest token    --> should not be accessed
    print(response.status_code)
    print(response.json())

def get_all_emps(token):
    response = requests.get(EMP_BASE_URI,headers = token) #guest token    --> should not be accessed
    print(response.status_code)
    print(response.json())

if __name__ == '__main__':

    get_token_for_user("ganesh","ganesh1234")


    print('___________________________________________________________________________')

    get_all_emps_without_token()

    print('___________________________________________________________________________')


    get_all_emps(dict_token_val3)
