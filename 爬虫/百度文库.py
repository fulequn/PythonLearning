# -*- coding: utf-8 -*-
"""
Created on Fri May 29 20:03:51 2020

@author: 23820
"""
#encoding:utf8
import sys
from selenium import webdriver
import time
 
def gethrefAndFilename(browser):
    # 打开百度文库的首界面
    browser.get("https://wenku.baidu.com/")
    # 通过ID找网页的标签，找到搜索框的标签
    seek_input = browser.find_element_by_id("kw")
    # 设置搜索的内容
    contents = "冀教版八年级下册数学期末检测题(含答案分析)"
    contents = str(contents).decode("utf8")
    seek_input.send_keys(contents)
    # 找到搜索文档按钮
    seek_but = browser.find_element_by_id("sb")
    # 并点击搜索文档按钮
    seek_but.click()
    # 文件标签集合
    list_href = []
    # 文件名称集合
    list_filename = []
    while True:
        # 获取所有的文档a标签，这里的elements指的是有多个元素,*表示的是任意的（在xpath中可以用）
        all_a = browser.find_elements_by_xpath("//*[@id=\"bd\"]/div/div/div[4]/div/dl[*]/dt/p[1]/a")
        for a in all_a:
            # print a.get_attribute("href")
            # print a.get_attribute("title")
            list_href.append(a.get_attribute("href"))
            list_filename.append(a.get_attribute("title"))
        # 获取body标签，的html
        body = browser.find_element_by_tag_name("body")
        body_html = body.get_attribute("innerHTML")
        # 判断下一页按钮是否存在
        flag = str(body_html).find("class=\"next\"")
        if flag != -1:
            # 获取下一页按钮的标签，这里用的是class标签，因为它只有一个
            next_page = browser.find_element_by_class_name("next")
            # 点击下一页
            next_page.click()
            # 点击之后，睡眠5s，防止页面没有加载完全，报no such element的错误
            time.sleep(5)
            break
        else:
            break
    return list_href,list_filename
 
def getContentsByHref(href,browser):
    browser.get(href)
    body = browser.find_element_by_tag_name("body")
    flag = str(body).find("id=\"html-reader-go-more\"")
    if flag != -1:
        # 找到继续阅读按钮的上一级div,banner-more-btn是div的类名用.,ID用#
        hidden_div = browser.find_element_by_css_selector("#html-reader-go-more")
        # 获取阅读按钮
        gotBtn = browser.find_element_by_css_selector("#html-reader-go-more .banner-more-btn")
        actions = webdriver.ActionChains(browser)
        actions.move_to_element(hidden_div)
        actions.click(gotBtn)
        actions.perform()
    time.sleep(3)
    # 获取包含内容的div
    div_text = browser.find_elements_by_class_name("ie-fix")
    for temp in div_text:
        text = temp.text
        print(text)
 
if __name__ == "__main__":
    browser = webdriver.Chrome()
    list_href, list_filename = gethrefAndFilename(browser)
    for href in list_href:
        getContentsByHref(href,browser)
 
 