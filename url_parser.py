from bs4 import BeautifulSoup
from pprint import pprint
import urllib.request

def search_urls(url):
    parser = 'html.parser'
    try:
        resp = urllib.request.urlopen(url)
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
        searched_url={"URL":url}
        URLS_found=[]
        for link in soup.find_all('a', href=True):
            if 'http' in link['href']:
                URLS_found.append(link['href'])
        searched_url["URLS Found"]= URLS_found
        return searched_url
    except urllib.error.HTTPError as e:
        return {"URL":f"{url} - This error was found - {e}"}
        # if e.getcode() == 404: # check the return code
        #     pprint(f'URL: {url} - returned 404 - NOT FOUND')
        #     return {"- returned 404 - NOT FOUND"}

def inception_search(search_results):
    inception=[]
    for links_found in search_results['URLS Found']:
        inception.append(search_urls(links_found))  
    return inception

def list_col(col):
    ls_col=[]
    for i in col.find():
        ls_col.append(i)
    return ls_col if len(ls_col) > 0 else "Collection Empty"



