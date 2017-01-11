import requests
from bs4 import BeautifulSoup
import threading
import time

def getIPs(page):
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1",
        "Host":"www.kuaidaili.com",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    }
    page = str(page)
    url = "http://www.kuaidaili.com/free/outha/"+page+"/"
    try:
        r = requests.get(url,headers = headers)
    except:
        time.sleep(5)
        getIPs(page)
        return
    soup = BeautifulSoup(r.text, 'lxml')
    ips = []
    for each in soup.findAll('tr'):
        if each.td is not None:
            ip = each.find('td', attrs={"data-title":"IP"}).text + ':' + each.find('td', attrs={"data-title":"PORT"}).text
            ips.append(ip)
    threads = []
    
    for each in ips:
        t = threading.Thread(target=isValid, args=(each,))
        t.daemon = True
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()

def isValid(ip):
    proxies = {
        'http' : ip,
        'https': ip
    }
    try:
        t = requests.get("http://www.baidu.com", proxies = proxies, timeout = 3).elapsed.total_seconds()
    except:
        return
    with filelock:
        global total
        f.write(ip+"\n")
        total+=1
    print('Validated: ',ip)  

if __name__ == '__main__':
    start_time = time.time()
    global f
    f = open("IPs.txt","w+")
    f.seek(0)
    f.truncate()
    global filelock 
    filelock = threading.Lock()
    threads = []
#     global total
    total = 0
    for i in range(1000):
        print('Starting on page ', i+1)
        t = threading.Thread(target=getIPs, args=(i+1,))
        t.daemon = True
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    f.close()
    print('Total ips collected: ', total)
    print("Total time: %s seconds" % (time.time() - start_time))