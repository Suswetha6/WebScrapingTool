#Name: Suswetha
#Official mail: suswetha.23bcs10166@sst.scaler.com


from bs4 import BeautifulSoup
import requests

print("Please paste the link of the the preferred product from Amazon and SnapDeal-")
#Function to scrape amazon data
def scrape_amazon_data(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find('span', {'id': "productTitle"}).get_text().strip()
        price = soup.find('span', {"class": "a-price-whole"}).get_text().strip()
        return title, price
    except requests.RequestException as e: #ERROR when request is not accepeted
        print(f"Error making request to {url}: {e}")
        return None, None
    except AttributeError as e:
        print(f"Error parsing HTML from {url}: {e}")#Error when element is not found
        return None, None

# Taking inputs from the user
url1 = input("Amazon Link: ")

# Describing the type of content needed
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

#Funtion to scrape snapdeal data
def scrape_snapdeal_data(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find('h1', {'class': 'pdp-e-i-head'}).get_text().strip()
        price = soup.find('span', {'class': 'pdp-final-price'}).get_text().strip()
        return title, price
    except requests.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return None, None
    except AttributeError as e:
        print(f"Error parsing HTML from {url}: {e}")
        return None, None

# Taking inputs from the user
url2 = input("SnapDeal Link: ")

# Describing the type of content needed
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}


# Call the function to scrape Amazon data
title1, price1 = scrape_amazon_data(url1, headers)
# Call the function to scrape SnapDeal data
title2, price2 = scrape_snapdeal_data(url2, headers)
#Truncating the size of the title for better readability
max_length = 30
truncated_amazon_title = title1[:max_length]
truncated_snapdeal_title =title2[:max_length]
print("These are the required details")
#printing the output in tabular form
print("Website\t\tTitle\t\t\t\tPrice")
print("Amazon\t\t{}\tRs.{}".format(truncated_amazon_title , price1))
print("SnapDeal\t{}\t{}".format(truncated_snapdeal_title, price2))



