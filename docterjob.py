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
urls_url = root_url + '/public/J1600Z109Z103_A0300Z1100Z1400_T2_P'

# 获取页面数据并存储成数组
def get_single_page_info(singleurl):
    data = []
    # data = {}
    response = requests.get(root_url+singleurl)
    soup = bs4.BeautifulSoup(response.content,"html.parser")
    # 职业
    if len(soup.select('div.process_engineertopbag h5')) == 1:
        # data['job'] = [a.string for a in soup.select('div.process_engineertopbag h5')]
        data.append([a.string for a in soup.select('div.process_engineertopbag h5')][0])
    else:
        # data['job'] = "None"
        data.append("None")
    # 城市
    if len(soup.select('div.process_engineer_fontstop i')) == 1:
        # data['city'] = [a.string for a in soup.select('div.process_engineer_fontstop i')]
        data.append([a.string for a in soup.select('div.process_engineer_fontstop i')][0])
    else:
        # data['city'] = "None"
        data.append("None")
    # 要求
    if len(soup.select('div.process_engineer_fontstop span:nth-of-type(2)')) == 1:
        # data['req'] = [a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(2)')]
        data.append([a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(2)')][0])
    else:
        # data['req'] = "None"
        data.append("None")
    # 学历
    if len(soup.select('div.process_engineer_fontstop span:nth-of-type(3)')) == 1:
        # data['edu'] = [a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(3)')]
        data.append([a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(3)')][0])
    else:
        # data['edu'] = "None"
        data.append("None")
    # 科室
    if len(soup.select('div.process_engineer_fontstop span:nth-of-type(4)')) == 1:
        # data['keshi'] = [a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(4)')]
        data.append([a.string for a in soup.select('div.process_engineer_fontstop span:nth-of-type(4)')][0])
    else:
        # data['keshi'] = "None"
        data.append("None")
    # 描述
    if len(soup.select('div.description_list p')) == 1:
        # data['intro'] = [a.string for a in soup.select('div.description_list p')]
        itr = [a.string for a in soup.select('div.description_list p')][0]
        # print(type(itr))
        if itr != None:
            data.append([a.string for a in soup.select('div.description_list p')][0])
        else :
            data.append("None")
    else:
        # data['intro'] = "None"
        data.append("None")
    # 公司
    if len(soup.select('a.postion_list_infor')) == 1:
        # data['company'] = [a.string for a in soup.select('a.postion_list_infor')]
        cmp = [a.string for a in soup.select('a.postion_list_infor')][0]
        if cmp != None:
            data.append(cmp.replace("\n",""))
        else:
            data.append("None")
    else:
        # data['company'] = "None"
        data.append("None")
    print(len(soup.select('div.postion_title_r p')))
    if len(soup.select('div.postion_title_r p')) == 5:
        # 属性
        if len(soup.select('div.postion_title_r p:nth-of-type(2) span')) == 1:
            tp = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(1) span')][0]
            # data['type'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(1) span')]
            data.append(tp)
        else:
            # data['type'] = "None"
            data.append("None")
        # 规模
        if len(soup.select('div.postion_title_r p:nth-of-type(3) span')) == 1:
            # data['guimo'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(2) span')]
            data.append([a.string for a in soup.select('div.postion_title_r p:nth-of-type(2) span')][0])
        else:
            # data['guimo'] = "None"
            data.append("None")
        # 招人数量
        if len(soup.select('div.postion_title_r p:nth-of-type(4) span')) == 1:
            # data['need'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(3) span')]
            data.append([a.string for a in soup.select('div.postion_title_r p:nth-of-type(3) span')][0])
        else:
            # data['need'] = "None"
            data.append("None")
        # 地址
        if len(soup.select('div.postion_title_r p:nth-of-type(5) span')) == 1:
            # data['address'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(4) span')]
            data.append([a.string for a in soup.select('div.postion_title_r p:nth-of-type(4) span')][0])
        else:
            # data['address'] = "None"
            data.append("None")
    else:
        # 属性
        if len(soup.select('div.postion_title_r p:nth-of-type(1) span')) == 1:
            tp = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(1) span')][0]
            # data['type'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(1) span')]
            data.append(tp)
        else:
            # data['type'] = "None"
            data.append("None")
        # 规模
        if len(soup.select('div.postion_title_r p:nth-of-type(2) span')) == 1:
            # data['guimo'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(2) span')]
            data.append([a.string for a in soup.select('div.postion_title_r p:nth-of-type(2) span')][0])
        else:
            # data['guimo'] = "None"
            data.append("None")
        # 招人数量
        if len(soup.select('div.postion_title_r p:nth-of-type(3) span')) == 1:
            # data['need'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(3) span')]
            data.append([a.string for a in soup.select('div.postion_title_r p:nth-of-type(3) span')][0])
        else:
            # data['need'] = "None"
            data.append("None")
        # 地址
        if len(soup.select('div.postion_title_r p:nth-of-type(4) span')) == 1:
            # data['address'] = [a.string for a in soup.select('div.postion_title_r p:nth-of-type(4) span')]
            data.append([a.string for a in soup.select('div.postion_title_r p:nth-of-type(4) span')][0])
        else:
            # data['address'] = "None"
            data.append("None")

    # 输出薪资
    if len(soup.select('div.process_engineer_fontstop p')) == 1:
        # data['salary'] = [a.string for a in soup.select('div.process_engineer_fontstop p')]
        # data.append([a.string for a in soup.select('div.process_engineer_fontstop p')][0])
        sl = [a.string for a in soup.select('div.process_engineer_fontstop p')][0]
        if sl != None:
            data.append(sl.replace("\n",""))
        else:
            data.append(sl)
    else:
        # data['salary'] = "None"
        data.append("None")
    # 招聘发布时间 time
    if len(soup.select('p.process_titlein')) == 1:
        data.append([a.string for a in soup.select('p.process_titlein')][0])
    else:
        # data['time'] = "None"
        data.append("None")
    print(data[8])
    return data

# 获取爬去页面的连接
pageurl = []
def get_page_urls(num):
    res = requests.get(urls_url+str(num)+'/')
    # if res.status_code == 200:
    if num < 2:
        info = "正在爬取第"+str(num)+"个网页链接"
        print(info.decode("utf-8"))
        
        urlsoup = bs4.BeautifulSoup(res.content,"html.parser")
        pageurl.extend([a.attrs.get('href') for a in urlsoup.select('span.job_name a[href^=/resume]')])
        get_page_urls(num+1)
    else:
        pass

# 并发处理
def multi_processing():
    pool = Pool(8)
    get_page_urls(1)
    results = pool.map(get_single_page_info, pageurl)
    with open('data.csv', 'wb') as csvfile:  
        spamwriter = csv.writer(csvfile, dialect='excel')  
        #设置标题  
        spamwriter.writerow(['job','city','req','edu','keshi','intro','company','type','guimo','need','address','salary','time'])  
        #将CsvData中的数据循环写入到CsvFileName文件中  
        print("write in csv")
        for item in results: 
            spamwriter.writerow(item)  

    

if __name__ == '__main__':
    multi_processing()

