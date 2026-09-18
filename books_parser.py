import requests
import pandas as pd
from bs4 import BeautifulSoup

data = []

for i in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    response.encoding = "utf-8"
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    books = soup.find_all("h3")
    prices = soup.find_all(class_="price_color")

    for b, p in zip(books, prices):
        name = b.find("a")["title"]
        price = p.text.strip()
        data.append({"Название": name, "Цена": price})

    print(f"Страница {i} готова")

df = pd.DataFrame(data)
df.to_excel("all_books.xlsx", index=False)
print("Готов!")