upper={'А':'A','Б':'B','Ҹ':'C','Ч':'Ç','Д':'D','Е':'E','Ә':'Ə','Ф':'F',\
    'Ҝ':'G','Ғ':'Ğ','Һ':'H','Х':'X','Ы':'I','И':'İ','Ж':'J','К':'K',\
        'Г':'Q','Л':'L','М':'M','Н':'N','О':'O','Ө':'Ö','П':'P','Р':'R',\
            'С':'S','Ш':'Ş','Т':'T','У':'U','Ү':'Ü','В':'V','Ј':'Y','З':'Z'}

lower={'а':'a','б':'b','ҹ':'c','ч':'ç','д':'d','е':'e','ә':'ə','ф':'f',\
    'ҝ':'g','ғ':'ğ','һ':'h','х':'x','ы':'ı','и':'i','ж':'j','к':'k','г':'q',\
        'л':'l','м':'m','н':'n','о':'o','ө':'ö','п':'p','р':'r','с':'s','ш':'ş',\
            'т':'t','у':'u','ү':'ü','в':'v','ј':'y','з':'z'}

sampleText = "Кирил графикалы Азәрбаyҹан әлфибасы"
text = input("Kiril qrafikalı yazını daxil edin: ")

if text == "":
	print("Örnək cümlə:", sampleText)
	text = sampleText

for i in text:
	if(i in lower):
		text = text.replace(i, lower.get(i))
	elif(i in upper):
		text = text.replace(i, upper.get(i))

print("Latın qrafikasında:", text)
