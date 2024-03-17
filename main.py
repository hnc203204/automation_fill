import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from get_sheet_information import *
from create_complain_file import *

def sleep(sec : int):
    time.sleep(sec)

def get_ele_by_xpath(explorer, value):
    return explorer.find_element(by=By.XPATH, value=value)

def login_vnu(explorer):
    email_fill = get_ele_by_xpath(explorer=explorer, value='// *[ @ id = "username"]')
    password_fill = get_ele_by_xpath(explorer=explorer, value='// *[ @ id = "password"]')
    submit = get_ele_by_xpath(explorer=explorer, value='// *[ @ id = "kc-login"]')
    email_fill.send_keys(os.getenv("MSV"))
    password_fill.send_keys(os.getenv("password"))
    submit.click()

def click_motion(ele):
    ele.click()
    sleep(1)
    ele.clear()

def exe():
    explorer = webdriver.Chrome()
    explorer.get("https://docs.google.com/forms/d/e/1FAIpQLSewG33FrS1zbQuAsvMkpiYbZPfgwKYJIqpK1dJvjyRC6AxpJw/viewform")
    sleep(2)
    button_login = get_ele_by_xpath(explorer=explorer, value="/html/body/div[2]/div/div[2]/div[3]/div[2]")
    button_login.click()
    email = os.getenv("mail")
    sleep(2)
    email_fill = get_ele_by_xpath(explorer=explorer, value='//*[@id="identifierId"]')
    email_fill.send_keys(email)
    confirm = get_ele_by_xpath(explorer=explorer, value='//*[@id="identifierNext"]/div/button')
    confirm.click()
    sleep(2)
    login_vnu(explorer)
    sleep(4)
    google_confirm = get_ele_by_xpath(explorer=explorer, value='//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
    google_confirm.click()
    sleep(3)
    with open("test.json","r") as file:
        all = json.load(file)
    scores = [
        "",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div',
    ]
    for x in all:

        explorer.get("https://docs.google.com/forms/d/e/1FAIpQLSewG33FrS1zbQuAsvMkpiYbZPfgwKYJIqpK1dJvjyRC6AxpJw/viewform")

        click_a = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div[1]/label')
        click_a.click()
        id_fill = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        click_motion(id_fill)
        id_fill.send_keys(x["id"])

        link_fill = get_ele_by_xpath(explorer,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        click_motion(link_fill)

        link_fill.send_keys(x["link_slide"])

        slide = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
        click_motion(slide)
        slide.send_keys(x["slides"])

        score = random.randint(8, 10)
        score_button = get_ele_by_xpath(explorer, scores[score])
        score_button.click()

        button_next = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        button_next.click()

        sleep(1)

        link_video_fill = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_video_fill.send_keys(x["link_video"])

        videos = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        videos.send_keys(x["videos"])

        score_video_button = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div')
        score_video_button.click()

        experience = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
        experience.send_keys(x["experience"])

        submit = get_ele_by_xpath(explorer, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
        submit.click()

        sleep(3)

    time.sleep(100)

def get_list_group():
    complain_list = []
    check = {}
    for x in read_file():
        new_complain = {}
        numerous = 0
        try:
            numerous = int(x["Nhóm được nhận xét"])
        except:
            continue

        # print(not numerous in check.keys())
        if not numerous in check.keys():
            new_complain = {
                "id" : x["Nhóm được nhận xét"],
                "link_slide": x["Liên kết đến slide nhận xét"],
                "slides": x["Nội dung nhận xét về slides"],
                "link_video": x["Liên kết đến video nhận xét"],
                "videos" : x["Nội dung nhận xét về video"],
                "score" : x["Chấm điểm (thang 10)"],
                "experience" : x["Viết một đoạn văn nêu lại những gì em còn nhớ được sau khi xem video và slides. (Ít nhất 2 câu.)"]
            }
            check[numerous] = 1
            complain_list.append(new_complain)

    test_file(complain_list)

if __name__ == "__main__":
    get_list_group()
    exe()
