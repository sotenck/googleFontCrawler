from crawler import FontCrawl

# Ask for Input
print("--------------------------------------------")
print("---- Google® Fonts local file extractor ----")
print("--------------------------------------------")

print("Welcome to Google®-Font local install helper!")


# Request URL Input
print("\nPlease copy your Google® fonts include URL here:")

googleBaseUrl = "fonts.googleapis.com/css?family="

fontUrl = str(input())

while(fontUrl.find(googleBaseUrl) < 0):
    print("Wrong Google®-Font URL - Try again!")
    print("\nInsert Google® Font include link:")
    fontUrl = str(input())

#fontUrl = "https://fonts.googleapis.com/css?family=Cormorant+Garamond:700,700i|Nunito+Sans:400,700,900"

print("... start webcrawler")
# Crawl URL and get List of used Fonts back
fontCrawl = FontCrawl(fontUrl)

print("... analyze data")
fontList = fontCrawl.textSegment()

# Work with DATA
import requests
import shutil
import os

base_path = "export"
font_path = "/fonts"

webPath = "src/fonts"

print("... cleaning environment")

#Remove previous Content
shutil.rmtree(base_path)
os.makedirs(base_path)
os.makedirs(base_path+font_path)



cssFileData = ""
headerPreload = ""
styleCount = 0;

for n in fontList:
    cssFileData += "/* "+n.name.upper()+" | "+n.charset+" */" + "\n"
    for m in n.variations:
        fileName = f"/{n.cleanFamilyName()}-{m.getFileAdding()}-{n.charset}.woff2"

        # Download Font-File To Disk
        r = requests.get(m.font)
        with open(base_path+font_path+fileName, 'wb') as fontFile:
            fontFile.write(r.content)

        # Add preload Syntax
        headerPreload += '<link as="font" rel="preload" type="font/woff2" href="./'+webPath+fileName+'" />' + "\n";

        # Add Font to CSS
        cssFileData += "/* "+m.getFileAdding()+" */" + "\n"
        cssFileData += "@font-face{" + "\n"
        cssFileData += "    font-family: '"+n.name+"';" + "\n"
        cssFileData += "    font-style: "+m.styleName+";" + "\n"
        cssFileData += "    font-weight: "+str(m.fontWeight)+";" + "\n"
        cssFileData += "    src: url('../"+webPath+fileName+"') format('woff2');" + "\n"
        cssFileData += "    unicode-range: "+n.unicode+";" + "\n"
        cssFileData += "}" + "\n"

        styleCount += 1

# link Font CSS File
headerPreload += '<link rel="preload stylesheet" as="style" href="./css/font.css"  />'

# Write CSS File
with open(base_path+'/font.css', 'wt') as cssFile:
    cssFile.write(cssFileData)
    print(f"Generated and exported css file");

# Write HTML FILE
with open(base_path+'/header.html', 'wt') as htmlFile:
    htmlFile.write(headerPreload)
    print(f"Generated and exported header html file");


# Success Status
print(f"Downloaded {styleCount} woff2 font files successfully");