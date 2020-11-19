import requests

url = "https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms1"

querystring = {"phonenum":"14168052749,15144305707","msg":"Hello, unfortunetly something went wrong... Please proceed http://134.122.29.252"}

headers = {
    'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
    'x-rapidapi-host': "sms-international.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
