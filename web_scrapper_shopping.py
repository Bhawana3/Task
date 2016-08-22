from lxml import html
import requests
from bs4 import BeautifulSoup

def get_url(keyword):
	url = "http://www.shopping.com/products?KW=" + str(keyword)
	return url

def get_soup(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text)
	return soup

def get_product_count(url):
    try:
        soup = get_soup(url)
        results_container = soup.find('div', attrs={'id': 'searchResultsContainer'})
        find_each_product = results_container.findAll('div', attrs={'class': 'gridItemTop'})
        return [url,len(find_each_product)]
    except Exception as e:
        return None

def get_next_page_link(List,url):
    try:
        soup = get_soup(url)
        next_page_link = soup.find('div', attrs={'class': 'paginationNew'})

        if soup is None or next_page_link is None:
            return None

        element = next_page_link.find('span', attrs={'class': 'paginationNext'})
        link = element.find('a', href=True)

        if element is None or link is None:
            return None


        next_page_link = base_url + link['href']
        print next_page_link
        List.append(next_page_link)
        # recursive call for getting next page
	get_next_page_link(List,next_page_link)
        return List
    except Exception as e:
        print e

def get_each_page_products(page_urlList):
    url_product_count = []
    if page_urlList is None:
        return None
    else:
        for page_url in page_urlList:
            url_count = get_product_count(page_url)
            print url_count
            url_product_count.append(url_count)
        return url_product_count

def get_total_results(url_list):
    if url_list is not None:
        return sum([results[1] for results in url_list])

def get_results():
    url = get_url(keyword)
    print ''
    print 'Listing all links:'
    print url
    page_urlList = get_next_page_link(List=[], url=url)

    print ''
    print "Getting products' count on each page ..."
    first_page_count = get_product_count(url)
    print first_page_count
    page_count = get_each_page_products(page_urlList)
    if page_count:
        page_count.insert(0,first_page_count)
        for count in page_count:
            print count
        print "Total number of results for the specified keyword -", get_total_results(page_count)

    else:
        if first_page_count is None:
            print "Total number of results for the specified keyword -", 0
        else:
            print "Total number of results for the specified keyword -", first_page_count[1]



# program starts from here
if __name__ == "__main__":
    base_url = 'http://www.shopping.com'
    keyword = raw_input("Enter keyword to search : ")
    print "You have entered :", keyword
    get_results()

