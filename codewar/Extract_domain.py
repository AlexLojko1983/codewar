"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example: * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
            * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
"""
url = "http://www.zombie-bites.com"
def domain_name(url):
    from urllib.parse import urlparse
    url1 = "https://"
    if url[0] != 'h':
        url = url1+url
    domen = urlparse(url).netloc
    if domen[:3] == 'www':
        domen = domen[4:]
    domen = domen[:domen.find('.')]
    return domen

domain_name(url)
print(domain_name(url))

