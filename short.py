import pyshorteners

s = pyshorteners.Shortener()

url_init = input("What URL may I shorten for you (^-^) ? : ")
url_shorten = s.tinyurl.short(url_init)

print("Shortened Link : ", url_shorten)
print("Great!", url_init, "has been shortened to", url_shorten)
