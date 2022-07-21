import urllib.request

def url_info():
    #print("환율 계산기 입니다.")
    page = urllib.request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8")
    text = page.read().decode('utf8')
    #f = open("D:/python-my/dist/url_read_text.txt", 'w', encoding='utf8')
    #f.write(text)
    #f.close()
    # print(text)

    where = text.find('class="grp_info"> <em>')
    # print(where)
    start_of_time = where + 22
    print("start_of_time:" + repr(start_of_time))
    end_of_time = start_of_time + 16
    prin = text[start_of_time:end_of_time]
    # prin = text[where:end_of_time]
    print(prin, "의 KEB 하나은행 환율정보 입니다.")
    return text

#EUR
def get_eur():
    text = url_info()
    eurwhere = text.find('<span>유럽연합 <em>EUR</em></span></a></th> <td><span>')
    eurletter = text[eurwhere+50] + text[eurwhere+52:eurwhere+58]
    print("유로: " + eurletter)
    return eurletter

#GBP
def get_gbp():
    text = url_info()
    gbpwhere = text.find('<span>영국 <em>GBP</em></span></a></th> <td><span>')
    gbpletter = text[gbpwhere+48] + text[gbpwhere+50:gbpwhere+56]
    print("영국 파운드: " + gbpletter)
    return gbpletter

get_eur()
get_gbp()
