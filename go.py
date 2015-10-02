import urllib2, re

urls = [
	"https://en.m.wikipedia.org/wiki/Pablo_Escobar",
	"https://en.m.wikipedia.org/wiki/Eazy-E",
	"https://en.m.wikipedia.org/wiki/Hannah_Montana",
	"https://en.m.wikipedia.org/wiki/Serena_Williams",
	"https://en.m.wikipedia.org/wiki/Ice_Cube",
	"https://en.m.wikipedia.org/wiki/Dr._Dre",
	"https://en.m.wikipedia.org/wiki/Labor_Day",
	"https://en.m.wikipedia.org/wiki/Narcos",
	"https://en.m.wikipedia.org/wiki/Straight_Outta_Compton_(2015_film)",
	"https://en.m.wikipedia.org/wiki/N.W.A",
	"https://en.m.wikipedia.org/wiki/Venus_Williams",
	"https://en.m.wikipedia.org/wiki/Welcome_Back_(film)",
	"https://en.m.wikipedia.org/wiki/Coca-Cola_formula",
	"https://en.m.wikipedia.org/wiki/Syrian_Civil_War",
	"https://en.m.wikipedia.org/wiki/Suge_Knight",
	"https://en.m.wikipedia.org/wiki/The_Visit_(2015_film)",
	"https://en.m.wikipedia.org/wiki/Whitey_Bulger",
	"https://en.m.wikipedia.org/wiki/Overview_effect",
	"https://en.m.wikipedia.org/wiki/Metal_Gear_Solid_V:_The_Phantom_Pain",
	"https://en.m.wikipedia.org/wiki/Aadesh_Shrivastava"
]

for index, url in enumerate(urls):
	response = urllib2.urlopen( url )
	html = response.read()

	# make the urls point to wikipedia.org
	html = re.sub( r"href=\"\/w\/load\.php", 'href="https://en.m.wikipedia.org/w/load.php', html )

	# generate normal page
	f = open('samples/%s-a.html'%index, 'w')
	f.write(html)
	f.close()

	srcsetstripper = re.compile( '/gi' )

	# generate stripped images page
	f = open('samples/%s-b.html'%index, 'w')
	html2 = re.sub( r"src=\"(.*\.)(png|jpg|jpeg)\"", "", html )
	html2 = re.sub( r"srcset=\"(.*)\"", "", html2 )
	f.write(html2)
	f.close()

	# generate just lead section page
	f = open('samples/%s-c.html'%index, 'w')
	re.DOTALL = True

	html3 = re.sub( '<h[1-9]>[\s\S]*<div class="post-content"', '<div class="post-content"', html )
	f.write(html3)
	f.close()
