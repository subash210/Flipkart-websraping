from bs4 import BeautifulSoup
import requests, openpyxl


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "laptops"
sheet.append(["lapname","lapprice"])

try:

    for a in range(1,10):

        response = requests.get(f"https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi3&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi7&page={a}")
        soup = BeautifulSoup(response.text, "html.parser")
        lap = soup.findAll("div",class_="_3pLy-c row")

        for i in lap:
            lapname = i.find("div", class_="_4rR01T").text
            lapprice = i.find("div",class_="_30jeq3 _1_WHN1").text
            print(lapname,lapprice)
            sheet.append([lapname,lapprice])
except:
    print("error")
excel.save("laptopdata.xlsx")