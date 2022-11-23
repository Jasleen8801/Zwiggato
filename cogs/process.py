import nextcord
from nextcord.ext import commands
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import asyncio


class ProcessCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @nextcord.slash_command(name="process", description="To process data from the food delivery website", guild_ids=[1040237301814546462])
    async def SetvalCity(self, interaction, website: str):
        if website.lower() == "zomato":
            await interaction.response.defer()
            await asyncio.sleep(25)
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT city, restaurant_name, food_item FROM main")
            result = cursor.fetchone()
            CITY_NAME, RESTAURANT_NAME, FOOD_NAME = result[0], result[1], result[2]
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

            options = Options()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument(f'user-agent={user_agent}')

            url = f"https://www.zomato.com/{CITY_NAME}/restoran"

            driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
            driver.get(url)

            dict = {}

            timeout = 10

            # driver.get_screenshot_as_file("screenshot.png")

            WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/header/nav/div/img')))
            time.sleep(3)

            search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/header/nav/ul[2]/li[1]/div/div/div[3]/input')
            search_bar.send_keys(RESTAURANT_NAME)
            search_bar.click()

            WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/header/nav/ul[2]/li[1]/div/div/div[3]/div[2]/div[1]')))
            time.sleep(2)

            first_option = driver.find_element(By.CLASS_NAME, 'sc-eNPDpu')
            first_option.click()

            WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/article/div/section/section')))

            order_online = driver.find_element(By.LINK_TEXT, 'Order Online')
            rest_link = order_online.get_attribute('href')
            dict['url'] = rest_link
            order_online.click()

            WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/section[4]/section/section[2]/div[2]/div/h2')))

            rest_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/section[3]/section/section/div/div/div/h1').text
            dict['name'] = rest_name

            rest_speciality = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/section[3]/section/section/div/div/section[1]/div')
            dict['speciality'] = rest_speciality.text

            offers = driver.find_elements(By.CLASS_NAME, 'sc-1a03l6b-3')
            dict['offers'] = []
            for offer in offers:
                dict['offers'].append(offer.text)

            search_menu = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/section[4]/section/section[2]/div[2]/section/section/input')
            search_menu.send_keys(FOOD_NAME)
            search_menu.click()

            time.sleep(2)

            names = driver.find_elements(By.CLASS_NAME, 'sc-1s0saks-15')
            prices = driver.find_elements(By.CLASS_NAME, 'sc-17hyc2s-1')

            dict["Food-items"] = []
            for name, price in zip(names, prices):
                dict['Food-items'].append(f"{name.text} - {price.text}")

            time.sleep(5)
            with open("Zomato.json", "w", encoding='utf-8') as fp:
                json.dump(dict, fp, indent=4)

            
            await interaction.followup.send("Zomato Data is Loaded")

            # await interaction.send("Zomato Data is Loaded. \nEnter the command `$result zomato` to view the result")

        elif website.lower() == "swiggy":
            await interaction.response.defer()
            await asyncio.sleep(25)
            options = Options()
            options.add_argument("--disable-gpu")
            options.add_argument('--disable-extensions')
            options.add_argument('--headless')

            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT city, restaurant_name, food_item FROM main")
            result = cursor.fetchone()
            CITY_NAME, RESTAURANT_NAME, FOOD_NAME = result[0], result[1], result[2]
            base_url = "https://www.swiggy.com"
            dict = {}
            timeout = 10
            driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
            driver.get(base_url)

            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div[2]')))

            city_input = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div/input')
            city_input.send_keys(CITY_NAME)

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, '_3lmRa')))

            find_city_button = driver.find_element(By.CLASS_NAME, '_3lmRa')
            find_city_button.click()

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, '_10p2-')))

            search_a_tag = driver.find_elements(By.CLASS_NAME, '_1T-E4')
            search_a_tag[3].click()

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/div')))

            input_rest = driver.find_element(By.CLASS_NAME, '_2FkHZ')
            input_rest.send_keys(RESTAURANT_NAME)

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, '_1VxLu')))

            first_choice = driver.find_element(By.CLASS_NAME, '_37IIF')
            first_choice.click()

            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[3]/div[1]')))

            rest_link_item = driver.find_element(By.CLASS_NAME, 'styles_container__fLC0R')
            link = rest_link_item.get_attribute('href')
            dict['url'] = link

            item_block = driver.find_element(By.CLASS_NAME, 'styles_containerRestaurant__3vhx3')
            item_block.click()

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/span[2]')))

            rest_name = driver.find_element(By.CLASS_NAME, '_3aqeL').text
            dict['name'] = rest_name

            rest_speciality = driver.find_element(By.CLASS_NAME, '_3Plw0').text
            dict['speciality'] = rest_speciality

            rest_offers = driver.find_elements(By.CLASS_NAME, '_3lvLZ')
            dict['offers'] = []
            for offer in rest_offers:
                dict['offers'].append(offer.text)

            search_item = driver.find_element(By.CLASS_NAME, '_5mXmk')
            search_item.send_keys(FOOD_NAME)

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/h2')))
            time.sleep(2)

            parent = driver.find_element(By.ID, 'h-2061393516')
            names = parent.find_elements(By.CLASS_NAME, 'styles_itemNameText__3ZmZZ')
            prices = parent.find_elements(By.CLASS_NAME, 'rupee')

            dict['Food-items'] = []

            for name, price in zip(names, prices):
                dict['Food-items'].append(f"{name.text} - {price.text}")

            driver.quit()

            with open("Swiggy.json", "w", encoding='utf-8') as fp:
                json.dump(dict, fp, indent=4)

            await interaction.followup.send("Swiggy Data is Loaded")
        else:
            embed = nextcord.Embed(title="ERROR", description=f'''
            We're currently working on trying to process the data from {website}.
            Please forgive us for the inconvenience caused.
            Kindly head of over to Help and Support Section for further assistance''')
            await interaction.send(embed=embed)

def setup(bot):
    bot.add_cog(ProcessCog(bot))
