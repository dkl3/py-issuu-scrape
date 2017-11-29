from bs4 import BeautifulSoup
import sys
import wget
import os
import urllib.request
import re
import subprocess

x = str(input("Enter the url: "))
howmanypages = int(input("How many pages? "))+1

for page in range(1, howmanypages):
    webpage = urllib.request.urlopen(x)
    soup = BeautifulSoup(webpage, 'html.parser')
    pagetitle = soup.find('meta', attrs={'property': 'og:title'})['content']
    
    imglink3 = soup.find('meta', attrs={'property': 'og:image'})['content']
    imglink2 = imglink3.replace('1.jpg','')
    imglink = imglink2 + str(page) + ".jpg"
    getimg = wget.download(imglink)
    print('Page {}: '.format(str(page)) + imglink + '\n')

    myfile = open('urls.txt', 'a')
    myfile.write("%s\n" % imglink)
    myfile.close()

    params = ['convert', 'page_*', pagetitle + '.pdf']
    subprocess.check_call(params)

    url_out = "URL: " + x
    description = soup.find('meta', attrs={'property': 'og:description'})['content']
    desc_out = "Description: " + description
    uploaded = soup.find('div', attrs={'class': 'DocumentInfo__date--2llaY'})['datetime']
    upload_out = "Uploaded: " + uploaded
    uploader = soup.find('div', attrs={'class': 'PublisherInfo__name--3j27Y'})
    uploadlink_out = "Uploader link: " + "https://issuu.com" + uploader.a['href']

    webpage2 = urllib.request.urlopen("https://issuu.com" + uploader.a['href'])
    soup2 = BeautifulSoup(webpage2, 'html.parser')
    uploadername = soup2.find('meta', attrs={'property': 'og:title'})['content']
    uploader_out = "Uploader: " + uploadername


    myfile2 = open('info.txt', 'w')
    myfile2.write(url_out + "\n" +uploader_out + "\n" + uploadlink_out + "\n" + desc_out + "\n" + upload_out)
    myfile2.close()

os.system('rm page_*')
