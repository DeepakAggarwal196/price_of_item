import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.amazon.in/dp/B00Y0R94PQ")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
# <span id="priceblock_ourprice" class="a-size-medium a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span> == $0 "7,200.00" </span>

string_price = element.text.strip() # "7,200"
price_without_comma_1 = string_price[0]
price_without_comma_2 = string_price[2:]
price_without_comma = price_without_comma_1 + price_without_comma_2
int_price = float(price_without_comma)
if int_price < 5000:
    buy=True
else:
    buy=False
if(buy):
    print("it is in budget")
elif(buy==False):
    print("it is out of budget")
print("the current price is {}".format(int_price))
