import os
import utils
import requests
import time
import random
import fpdf
import ocrmypdf
from alive_progress import alive_it

# DISCLAIMERS
# This script should only be run if you own the book
# This script is for educational purposes only
# This script is not intended to be used for piracy
# This script is not intended to be used for any illegal activities
# This script is not intended to be used for any commercial activities
# Only for students who don't want to deal with the always online nature of the books and a searchable (OCR) version
# I am not responsible for any misuse of this script or any legal actions taken against you for using this script

# There's 3 sizes for the pages, small, medium or large
# You can change the size by changing the URL of the page to the desired size in utils.py
# For medium it's avg 8MB per 100 pages (non OCR)

# CONFIG
outputFolder = 'res/'
beginPrefix = 173585 # the prefix of the first page of the book

bookID = 497 # check the URL of the book
baseURL = f'www.iplusinteractif.com/media/iplus/book_content/{bookID}/'
pageIDs = utils.getBookIDs()

# AUTH
cookie = """INSERT COOKIE HERE""" # check the request headers of the book page for the cookie

# HTTP HEADERs

headers = {
    "Host": 'www.iplusinteractif.com',
    "Connection": 'keep-alive',
    "Accept": 'image/avif,image/webp,*/*',
    "Accept-Encoding": 'gzip, deflate, br',
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    "Cookie": cookie,
    "Referer": 'https://www.iplusinteractif.com/books/276/497/173654?userRole=student',
    "Accept-Language": 'en-US,en;q=0.5',
    "Priority" : 'u=4',
    "Sec-Fetch-Dest": 'image',
    "Sec-Fetch-Mode": 'no-cors',
    "Sec-Fetch-Site": 'same-origin',
    "TE": 'trailers',
}

def cleanOutput(folder):
    filesToDelete = os.listdir(folder)
    for file in filesToDelete:
        if os.path.isfile(folder + file):
            print("REMOVING: " + folder + file)
            os.remove(folder + file)
def encodeReferer(pageIDs, pageID):
    index = pageIDs.index(pageID)
    if index == 0:
        return f'https://www.iplusinteractif.com/books/276/{bookID}/{beginPrefix}?userRole=student'
    else:
        return f'https://www.iplusinteractif.com/books/276/{bookID}/{beginPrefix+index}?userRole=student'

def downloadPage(pageID, folder, headers):
    ref = encodeReferer(pageIDs, pageID)
    headers['Referer'] = ref
    headers_utf8 = {k: v.encode('utf-8') for k, v in headers.items()}
    req = requests.get(f'https://{baseURL}{pageID}', headers=headers_utf8)
    print(f"Downloading {pageID}")
    if requests.status_codes.codes.ok != req.status_code:
        print(f"Error downloading {pageID}, status code: {req.status_code}, exiting...")
        return
    with open (folder + pageID, 'wb') as f:
        f.write(req.content)
        f.close()
    time.sleep(0.5*random.random()+1) # we wait for a bit to avoid getting rate limited

def downloadAllPages():
    begin = 0
    end = len(pageIDs)
    listArray=list(range(begin, end))
    random.shuffle(listArray)
    bar = alive_it(listArray)
    for i in bar:
        downloadPage(pageIDs[i], outputFolder, headers)


def makePDF(pageIDs, folder):
    pdfIterateCount = 0
    pdf = fpdf.FPDF(format=(648, 783))
    bar = alive_it(pageIDs)
    for pageID in bar:
        pdfIterateCount += 1
        # print(f"Adding page {pageID} to PDF, {len(pageIDs)-pdfIterateCount} pages left to add.")
        pdf.add_page()
        pdf.image(folder + pageID, 0, 0, 648, 783)
    try:
         pdf.output(folder + "book.pdf", "F")
    except Exception as e:
        print("Error making PDF, exiting...")
        print(e)
        exit()

def OCRPDF():
    ocrmypdf.ocr(outputFolder + "book.pdf", outputFolder + "book.pdf", language='fra')

def main():
    # cleanOutput(outputFolder)
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    if os.path.exists(outputFolder + "book.pdf"):
        print("PDF already exists, exiting...")
        exit()
    print("Downloading pages...")
    downloadAllPages()
    print("Making PDF...")
    makePDF(pageIDs, outputFolder)
    print("OCR PDF...")
    OCRPDF()
    print(f"Done! PDF saved to {outputFolder}book.pdf.")

if __name__ == "__main__":
    main()
