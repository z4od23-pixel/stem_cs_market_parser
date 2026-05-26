from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Chrome()
browser.get("https://steamcommunity.com/market/search?appid=730")

time.sleep(2)

button_exit_beta = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/button")
button_exit_beta.click()
time.sleep(1)
button_to_cs2 = browser.find_element(By.CSS_SELECTOR,"a[href='https://steamcommunity.com/market/search?appid=730']")
button_to_cs2.click()
al_summ = 0
time.sleep(2)
x = 0
while x < 3141:
#ЧИСЛО СКИНОВ ДАННОГО ТИПА
    counts_html = browser.find_elements(By.CSS_SELECTOR,"span[class='market_listing_num_listings_qty']")
    counts_list = []
    for element in counts_html :
        counts_list.append(element.text)
    counts_list_new = []
    for elements in counts_list:
        text = elements.replace(",","")
        counts_list_new.append(int(text)) 

#СТОИМОСТЬ СКИНОВ ДАННОГО ТИПА
    prices_html = browser.find_elements(By.CSS_SELECTOR,"span[class='normal_price']")
    prices_list = []
    for element in prices_html:
        prices_list.append(element.text)
    prices_list_new = []
    if prices_list[0][-1] == ".":
        for element in prices_list:
            text_list = element.split(" ")
            text = text_list[0]
            text1 = text.replace(",",".")
            prices_list_new.append(float(text1))
    else :
        for element in prices_list:
            text_list = element.split(" ")
            text = text_list[0][1:]
            prices_list_new.append(float(text))

    i = 0
    page_summ = 0
    while i < 10:
        if prices_list[0][-1] == ".":
            page_summ += counts_list_new[i] * prices_list_new[i]
        else :
            page_summ += counts_list_new[i] * prices_list_new[i] * 71
        i +=1

    al_summ += page_summ
    print('\n\n\n\n\n\n\n\n')
    print(f"Общая стоимость :{al_summ} рублей")
    print(f"Страниц отсканированно : {x+1}")
    next_button = browser.find_element(By.CSS_SELECTOR,"span[id='searchResults_btn_next']")
    next_button.click()
    x += 1
    time.sleep(2)
browser.quit()

#Изменение!