#encoding:utf-8
import requests
import bs4
from multiprocessing import Pool
import argparse
import re
import csv

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

# root_url为爬取网站，urls_url为信息列表（为获取url）
root_url = 'http://www.doctorjob.com.cn'
urls_url = [ '/public/J9900Z1500_A0300Z1100Z1400_T2_P',
'/public/J1018Z1006Z100_A0300Z1100Z1400_T2_P', 
'/public/J1200Z1400Z1029_A0300Z1100Z1400_T2_P', 
'/public/J1600Z109Z103_A0300Z1100Z1400_T2_P', 
'/public/J9900Z1500_A1500Z2600Z2700_T2_P', 
'/public/J1029Z1400Z1200_A1500Z2600Z2700_T2_P', 
'/public/J103Z109Z1600_A1500Z2600Z2700_T2_P', 
'/public/J1018Z1006Z100_A1500Z2600Z2700_T2_P', 
'/public/J1018Z1006Z100_A3400Z0700Z1000_T2_P', 
'/public/J1600Z109Z103_A3400Z0700Z1000_T2_P', 
'/public/J1200Z1400Z1029_A3400Z0700Z1000_T2_P', 
'/public/J9900Z1500_A3400Z0700Z1000_T2_P', 
'/public/J1029Z1400Z1200_A1300Z1600Z1700_T2_P', 
'/public/J9900Z1500_A1300Z1600Z1700_T2_P', 
'/public/J103Z109Z1600_A1300Z1600Z1700_T2_P', 
'/public/J100Z1006Z1018_A1300Z1600Z1700_T2_P', 
'/public/J100Z1006Z1018_A1800Z1900Z2200_T2_P', 
'/public/J1600Z109Z103_A1800Z1900Z2200_T2_P', 
'/public/J1200Z1400Z1029_A1800Z1900Z2200_T2_P', 
'/public/J9900Z1500_A1800Z1900Z2200_T2_P', 
'/public/J9900Z1500_A2400Z0900Z1200_T2_P', 
'/public/J1029Z1400Z1200_A2400Z0900Z1200_T2_P', 
'/public/J103Z109Z1600_A2400Z0900Z1200_T2_P', 
'/public/J1018Z1006Z100_A2400Z0900Z1200_T2_P', 
'/public/J1018Z1006Z100_A2000Z2100Z2300_T2_P', 
'/public/J1600Z109Z103_A2000Z2100Z2300_T2_P', 
'/public/J1200Z1400Z1029_A2000Z2100Z2300_T2_P', 
'/public/J9900Z1500_A2000Z2100Z2300_T2_P', 
'/public/J9900Z1500_A2800Z2900Z3200_T2_P', 
'/public/J1029Z1400Z1200_A2800Z2900Z3200_T2_P', 
'/public/J103Z109Z1600_A2800Z2900Z3200_T2_P', 
'/public/J1018Z1006Z100_A2800Z2900Z3200_T2_P', 
'/public/J1018Z1006Z100_A0800Z2500Z3000_T2_P', 
'/public/J1600Z109Z103_A0800Z2500Z3000_T2_P', 
'/public/J1200Z1400Z1029_A0800Z2500Z3000_T2_P', 
'/public/J9900Z1500_A0800Z2500Z3000_T2_P', 
'/public/J9900Z1500_A3300Z3500_T2_P', 
'/public/J1029Z1400Z1200_A3300Z3500_T2_P', 
'/public/J109Z103Z1600_A3300Z3500_T2_P', 
'/public/J1018Z1006Z100_A3300Z3500_T2_P']

# 获取页面数据并存储成数组
def get_single_page_info(singleurl):
    data = []
    response = requests.get(root_url+singleurl)
    soup = bs4.BeautifulSoup(response.content,"html.parser")
    # 职业
    if len(soup.select('div.process_engineertopbag h5')) == 1:
        data.append([a.string for a in soup.select('div.process_engineertopbag h5')][0])
    else:
        data.append("")
    # 城市
    if len(soup.select('div.process_engineer_fontstop i')) == 1:
        data.append([a.string for a in soup.select('div.process_engineer_fontstop i')][0])
    else:
        data.append("")
    # 要求
    if len(soup.select('div.process_engineer_fontstop span:nth-of-type(2)')) == 1:
        data.append([a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(2)')][0])
    else:
        data.append("")
    # 学历
    if len(soup.select('div.process_engineer_fontstop span:nth-of-type(3)')) == 1:
        data.append([a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(3)')][0])
    else:
        data.append("")
    # 科室
    if len(soup.select('div.process_engineer_fontstop span:nth-of-type(4)')) == 1:
        data.append([a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(4)')][0])
    else:
        data.append("")
    # 描述
    if len(soup.select('div.description_list p')) == 1:
        itr = [a.string for a in soup.select('div.description_list p')][0]
        if itr != None:
            data.append([a.string for a in soup.select('div.description_list p')][0])
        else :
            data.append("")
    else:
        data.append("")
    # 公司
    if len(soup.select('a.postion_list_infor')) == 1:
        cmp = [a.string for a in soup.select('a.postion_list_infor')][0]
        if cmp != None:
            data.append(cmp.replace("\n",""))
        else:
            data.append("")
    else:
        data.append("")
    # 输出薪资
    if len(soup.select('div.process_engineer_fontstop p')) == 1:
        sl = [a.string for a in soup.select('div.process_engineer_fontstop p')][0]
        if sl != None:
            data.append(sl.replace("\n",""))
        else:
            data.append(sl)
    else:
        data.append("")
    # 招聘发布时间 time
    if len(soup.select('p.process_titlein')) == 1:
        data.append([a.string for a in soup.select('p.process_titlein')][0])
    else:
        data.append("")
    # 属性
    if len(soup.select('div.postion_title_r img[src=/images/position/icom_leftin.png]')) == 1:
        tp = [a.string for a in soup.select('div.postion_title_r img[src=/images/position/icom_leftin.png]')][0]
        data.append(tp)
    else:
        data.append("")
    # 规模
    if len(soup.select('div.postion_title_r img[src=/images/position/icom_li.jpg]')) == 1:
        gm = [a.string for a in soup.select('div.postion_title_r img[src=/images/position/icom_li.jpg]')][0]
        data.append(gm)
    else:
        data.append("")
    # 招人数量
    if len(soup.select('div.postion_title_r img[src=/images/position/icom_job.jpg]')) == 1:
        nd = [a.string for a in soup.select('div.postion_title_r p span a')][0]
        data.append(nd)
    else:
        data.append("")
    # 地址
    if len(soup.select('div.postion_title_r img[src=/images/position/icom_map.jpg]')) == 1:
        data.append([a.string for a in soup.select('div.postion_title_r span[title]')][0])
    else:
        data.append("")
    # print(type(data))
    # return data
    write_in_csv(data)

# 获取爬去页面的连接
pageurl = []
def get_page_urls(num,un):
    res = requests.get(root_url+urls_url[un]+str(num)+'/')
    # if res.status_code == 200:
    max_num = get_max_num(root_url+urls_url[un])
    if num <= max_num:
        info = "正在爬取第"+str(num)+"个网页链接"
        print(info.decode("utf-8"))
        urlsoup = bs4.BeautifulSoup(res.content,"html.parser")
        pageurl.extend([a.attrs.get('href') for a in urlsoup.select('span.job_name a[href^=/resume]')])
        get_page_urls(num+1,un)
    else:
        if len(urls_url) > un+1:
            print("second_page_url")
            get_page_urls(1,un+1)
        else:
            pass

# 获取最大列表链接数目
def get_max_num(url):
    res = requests.get(url+'1/')
    urlsoup = bs4.BeautifulSoup(res.content,"html.parser")
    if len(urlsoup.select('div.fanye a[href^=/public]')) > 0:
        lasturl = [a.attrs.get('href') for a in urlsoup.select('div.fanye a[href^=/public]')][-1]
        max_str = re.findall(r'_P(.+?)/',lasturl)
        return int(max_str[0])
    else:
        return 0

# 并发处理
def multi_processing():
    pool = Pool(8)
    get_page_urls(1,0)
    pool.map(get_single_page_info, pageurl)
    # results = pool.map(get_single_page_info, pageurl)  

# 写入csv文件
def write_in_csv(info):
    with open('data.csv', 'a') as csvfile:  
        spamwriter = csv.writer(csvfile, dialect='excel')  
        #设置标题  
        # spamwriter.writerow(['job','city','req','edu','keshi','intro','company','salary','time','type','guimo','need','address'])  
        #将CsvData中的数据循环写入到CsvFileName文件中  
        print("write in")
        spamwriter.writerow(info)
    

if __name__ == '__main__':
    multi_processing()

