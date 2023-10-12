from bs4 import BeautifulSoup
import os

cmd='cd "the pages" && dir'
res = os.popen(cmd).read()

page_number = len(res.split(".htm"))-1


for n in range(page_number):

    #file = input('enter your amazon page : ')
    with open(f"the pages\\Amazon.com{n}.htm","r", encoding="utf-8") as html:
        soup = BeautifulSoup(html, 'lxml')
    
    
    produits = soup.find("div",{'class':'sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16'})
    
    produit_len = produits.find_all("div",{'class':'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})
    
    for i in range(len(produit_len)):
        
        #explor data
        print(str(n+1)+"/"+str(i+1))
        produit_title = produits.find_all("div",{'class':'a-section a-spacing-none a-spacing-top-small s-title-instructions-style'})
        title = produit_title[i].text.strip().replace('"',"`").replace("'","`")
        #print("title : ", title)
        produit_price = produits.find_all("div",{'class':'a-section a-spacing-small puis-padding-left-small puis-padding-right-small'})
        try :
            price = produit_price[i].find("span",{'class':'a-offscreen'}).text.strip()
            #print("price : ", price)
        except:
            price = "Null"
            #print("price : ", price)
        page_url = produits.find_all("a",{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        page = 'www.amazon.com'+str(page_url[i]).split('href="')[1].split('">')[0]
        #print("page : ", page)
        image_url = produits.find_all("div",{'class':'a-section aok-relative s-image-square-aspect'})
        image = str(image_url[i].img).split('src="')[1].split(' ')[0][0:-1]
        #print("image : ", image)
        #print("\n")
        
        title = '"'+title+'"'
        head = "Title,Price,Page,Image\n"
        line = f"{title},{price},{page},{image}"
        
        #saving in file csv
        if os.path.exists("produits.csv") is False:
            with open("produits.csv","w",encoding="utf-8") as file:
                file.writelines(head)
                file.writelines(line)
        else :
            with open("produits.csv","a",encoding="utf-8") as file:
                file.writelines("\n")
                file.writelines(line)
            
        