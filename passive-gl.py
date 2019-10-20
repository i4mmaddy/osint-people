#fb_search
def add(request):
    fb_dork="site:facebook.com "
    keyword = request.POST['n1']
    query = fb_dork + keyword

    print (query)
    d = {}
    i = 0
    
    for j in search(query, tld="co.in", num=10, start=0, stop=10, pause=2): 
        
        soup = BeautifulSoup(requests.get(j,'html.parser').text)
        
        if soup is not None:
            a = soup.title.string
        else:
            inc = "No title" + i
            i =+ 1 
        inc = a
        d[inc] = j
    
    print(d)
    return  render(request,'index.html',{'d': d })



#twitter_add
def twitteradd(request):
    tw_dork="site:twitter.com "
    keyword = request.POST['n1']
    query = tw_dork + keyword

    print (query)
    d = {}
    
    for j in search(query, tld="co.in", num=5, start=0, stop=5, pause=2): 
        soup = BeautifulSoup(requests.get(j,'html.parser').text)
        if soup is not None: 
            a =  soup.findAll('img', {'class': 'ProfileAvatar-image'})
            for image in a:
                d[image['src']] = j

        else:
            print("none type error")
            

    return  render(request,'demo.html',{'d': d })
