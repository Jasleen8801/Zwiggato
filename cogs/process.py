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
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)


class ProcessCog(commands.Cog):
    def __init__(self, bot, driver) -> None:
        self.bot = bot
        self.driver = driver

    async def process_zomato(self, city_name, rest_name, food_name):
        timeout = 10
        url = f"https://www.zomato.com/{city_name}/restoran"
        dict_data = {}

        self.driver.get(url)

        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/header/nav/div/img')))
        time.sleep(3)

        search_bar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/header/nav/ul[2]/li[1]/div/div/div[3]/input')
        search_bar.send_keys(rest_name)
        search_bar.click()

        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/header/nav/ul[2]/li[1]/div/div/div[3]/div[2]/div[1]')))
        time.sleep(2)

        first_option = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/header/nav/ul[2]/li[1]/div/div/div[3]/div[2]/div[1]')
        first_option.click()

        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/section[3]/section')))

        order_online = self.driver.find_element(By.LINK_TEXT, 'Order Online')
        rest_link = order_online.get_attribute('href')
        dict_data['url'] = rest_link
        order_online.click()

        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/section[4]/section/section[2]/div[2]/div/h2')))

        rest_name = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/section[3]/section/section/div/div/div/h1').text
        dict_data['name'] = rest_name

        rest_speciality = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/section[3]/section/section/div/div/section[1]/div')
        dict_data['speciality'] = rest_speciality.text

        offers = self.driver.find_elements(By.CLASS_NAME, 'sc-1a03l6b-3')
        dict_data['offers'] = []
        for offer in offers:
            dict_data['offers'].append(offer.text)

        search_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/section[4]/section/section[2]/div[2]/section/section/input')
        search_menu.send_keys(food_name)
        search_menu.click()

        time.sleep(2)

        names = self.driver.find_elements(By.CLASS_NAME, 'sc-1s0saks-15')
        prices = self.driver.find_elements(By.CLASS_NAME, 'sc-17hyc2s-1')

        # self.driver.quit()

        dict_data["Food-items"] = []
        for name, price in zip(names, prices):
            dict_data['Food-items'].append(f"{name.text} - {price.text}")

        time.sleep(3)
        with open("Zomato.json", "w", encoding='utf-8') as fp:
            json.dump(dict_data, fp, indent=4)

        return dict_data


    async def process_swiggy(self, city_name, rest_name, food_name):
        timeout = 10
        url = "https://www.swiggy.com"
        dict = {}

        self.driver.get(url)

        WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div[2]')))

        city_input = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div/input')
        city_input.send_keys(city_name)

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, '_3lmRa')))

        find_city_button = self.driver.find_element(By.CLASS_NAME, '_3lmRa')
        find_city_button.click()

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, '_10p2-')))

        # to do around here 
        search_a_tag = self.driver.find_elements(By.CLASS_NAME, '_1T-E4')
        search_a_tag[3].click()

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/div')))

        input_rest = self.driver.find_element(By.CLASS_NAME, '_2FkHZ')
        input_rest.send_keys(rest_name)

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, '_1VxLu')))

        first_choice = self.driver.find_element(By.CLASS_NAME, '_37IIF')
        first_choice.click()

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[3]/div[1]')))

        rest_link_item = self.driver.find_element(By.CLASS_NAME, 'styles_container__fLC0R')
        link = rest_link_item.get_attribute('href')
        dict['url'] = link

        item_block = self.driver.find_element(By.CLASS_NAME, 'styles_containerRestaurant__3vhx3')
        item_block.click()

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/span[2]')))

        rest_name = self.driver.find_element(By.CLASS_NAME, '_3aqeL').text
        dict['name'] = rest_name

        rest_speciality = self.driver.find_element(By.CLASS_NAME, '_3Plw0').text
        dict['speciality'] = rest_speciality

        rest_offers = self.driver.find_elements(By.CLASS_NAME, '_3lvLZ')
        dict['offers'] = []
        for offer in rest_offers:
            dict['offers'].append(offer.text)

        search_item = self.driver.find_element(By.CLASS_NAME, '_5mXmk')
        search_item.send_keys(food_name)

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/h2')))
        time.sleep(2)

        parent = self.driver.find_element(By.ID, 'h-2061393516')
        names = parent.find_elements(By.CLASS_NAME, 'styles_itemNameText__3ZmZZ')
        prices = parent.find_elements(By.CLASS_NAME, 'rupee')

        dict['Food-items'] = []

        for name, price in zip(names, prices):
            dict['Food-items'].append(f"{name.text} - {price.text}")

        # driver.quit()

        with open("Swiggy.json", "w", encoding='utf-8') as fp:
            json.dump(dict, fp, indent=4)

        return dict

    @nextcord.slash_command(name="process", description="To process data from the food delivery website", guild_ids=[GUILD_ID])
    async def SetvalCity(self, interaction, website: str):
        await interaction.response.defer()
        await asyncio.sleep(25)
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT city, restaurant_name, food_item FROM main")
        all_records = cursor.fetchall()

        if(len(all_records) >= 2):
            second_record = all_records[1]
            CITY_NAME, RESTAURANT_NAME, FOOD_NAME = second_record[0], second_record[1], second_record[2]
            print(f"{CITY_NAME} {RESTAURANT_NAME} {FOOD_NAME}")
        else: 
            print("Some issue")

        if website.lower() == "zomato":
            dict_data = await self.process_zomato(CITY_NAME, RESTAURANT_NAME, FOOD_NAME)
            await interaction.followup.send("Zomato Data is Loaded. \nEnter the command `/result zomato` to view the result")

        elif website.lower() == "swiggy":
            dict_data = await self.process_swiggy(CITY_NAME, RESTAURANT_NAME, FOOD_NAME)
            await interaction.followup.send("Swiggy Data is Loaded")

        else:
            embed = nextcord.Embed(title="ERROR", description=f'''
            We're currently working on trying to process the data from {website}.
            Please forgive us for the inconvenience caused.
            Kindly head of over to Help and Support Section for further assistance''')
            await interaction.send(embed=embed)

def setup(bot):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    bot.add_cog(ProcessCog(bot, driver))
