# Python - 3.6.0

remove_url_anchor = lambda url: url[:(('#' in url) and url.index('#')) or len(url)]
