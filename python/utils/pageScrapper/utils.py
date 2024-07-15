import re
size = 'm' # s, m, l
bookURLs = [
    'https://www.iplusinteractif.com/media/iplus/...', # only for that website, replace the url with the urls obtained below
]
# to get bookURLs
# 1. Go to the book page
# 2. Scroll the thumbnails all the way to the bottom to load all the images
# 3. Open the console
# 4. Run the following code:
# let e = document.querySelectorAll('.iplus-l-ReactPreviewFrame__paginationThubImg');
# let urls = [];
# for (const i of e) {
#     urls.push(i.src);
# }
# console.log(urls);
# 5. Copy the output and paste it in the list above (in Chrome/Chromium based as Firefox doesn't copy the full list)
def getBookIDs():
    found = []
    pattern = r'[\w-]+_\d+'
    for url in bookURLs:
        match = re.search(pattern, url)
        if match:
            match = match.group(0) + f'_{size}.png'
            found.append(match)
    return found
