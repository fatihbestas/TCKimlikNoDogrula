import requests
import xml.etree.ElementTree as ET

# SOAP request URL
url = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx"

# Structured XML for TC verification
payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
      <TCKimlikNo>TC_KIMLIK_NO_HERE</TCKimlikNo>
      <Ad>FIRST_NAME_HERE</Ad>
      <Soyad>LAST_NAME_HERE</Soyad>
      <DogumYili>DOGUM_YILI_HERE</DogumYili>
    </TCKimlikNoDogrula>
  </soap:Body>
</soap:Envelope>"""

# Headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://tckimlik.nvi.gov.tr/WS/TCKimlikNoDogrula'
}

print("TC:")
tc = input()
print("Ad:")
ad = input()
print("Soyad")
soyad = input()
print("Dogum yili")
dogum_yili = input()


# Replace placeholders with actual values
payload = payload.replace("TC_KIMLIK_NO_HERE", tc)  # Replace with actual TC Kimlik No
payload = payload.replace("FIRST_NAME_HERE", ad)  # Replace with actual first name
payload = payload.replace("LAST_NAME_HERE", soyad)  # Replace with actual last name
payload = payload.replace("DOGUM_YILI_HERE", dogum_yili)  # Replace with actual birth year

# print(payload)

# POST request
# encode('utf-8') is required for Turkish character support
response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))


# Prints the response
# print(response.text)

# Parse XML response
root = ET.fromstring(response.text)

# Get the content of the <TCKimlikNoDogrulaResult> tag
result = root.find('.//{http://tckimlik.nvi.gov.tr/WS}TCKimlikNoDogrulaResult').text

if result == 'true':
    print("Doğru")
else:
    print("Yanlış")

input()
