import re
texto = "o site do google é https://www.google.com e o site do facebook é https://www.facebook.com"
padrao= r"https?://\S+"
urls = re.findall(padrao, texto)
print(urls)