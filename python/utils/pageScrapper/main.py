import os
import utils
import requests
import time
import random

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
    with open (folder + pageID, 'wb') as f:
        f.write(req.content)
        f.close()
    time.sleep(0.5*random.random()+1) # we wait for a bit to avoid getting rate limited
