import requests
import json

api_url = ('https://api.exchangerate.host/latest')

gunluk_Doviz = input("Günlük Verileri Görmek İçin Herhangi Bir Tuşa Basınız: ")

result = requests.get(api_url)
result = json.loads(result.text)
print(result)




# miktar = (f"Ne Kadar Döviz {bozulan_döviz} Bozdurmak İstiyorsunuz: ")
# print("1 {0}={1} {2}".format(bozulan_döviz,result['base'],[alinan_döviz],alinan_döviz))
# print("{0} {1}={2}".format(miktar,bozulan_döviz,miktar*result['base'],[alinan_döviz],alinan_döviz))

