import webbrowser, sys, requests, bs4

print "Googling your search..."

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
relvnt_links = soup.select("h3.r a")

for i in range(1,5):
	print webbrowser.open('http://google.com' + relvnt_links[i].get("href"))
