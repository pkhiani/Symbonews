from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests

from csv import writer
#


def basic(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        # symbol = input("Enter a symbol you want to find the news for: ")
        if len(name) >= 1:
            url = 'https://finviz.com/quote.ashx?t='

            res = requests.get(url + name, headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.text, "html.parser")

            articles = soup.find_all("table", {"class": "fullview-news-outer"})

            for newsElement in articles:
                rows = newsElement.find_all('tr')
                # print(rows)
                lst = []

                for row in rows:
                    link = row.find("a", {"class": "tab-link-news"})['href']
                    article_name = row.find("div", {"class": "news-link-left"}).get_text().strip()
                    source = row.find("div", {"class": "news-link-right"}).get_text().strip()
                    details = row.find('td').get_text().strip()

                    content = article_name + " " + link + " " + details + " " + source
                    lst.append(str(content))

                return HttpResponse(lst)
        else:
            return HttpResponse("please enter valid symbol")
    return render(request, 'basic.html')

# def basic(request):
#     if request.method == 'POST':
#         name=request.POST.get('name','')
#         #code to check palindrome
#         if len(name) >= 1:
#             return HttpResponse("this is palindrome")
#         else:
#             return HttpResponse("given strong is not palindrome")
#
#     return render(request, 'basic.html')
# # Create your views here.





