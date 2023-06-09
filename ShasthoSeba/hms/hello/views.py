from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Doctor
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import json
import re


def home(request):
    return HttpResponse("Hello World!")


def doctors(request):
    dcs = Doctor.objects.all()
    dcs_data = []

    for i in dcs:
        dcs_data.append({
            'id': i.id,
            'name': i.name,
            'degree': i.degree,
            'specialist': i.specialist,
            'image_path': i.image_path,
            'hospital': i.hospital
        })

    return JsonResponse({'doctors': dcs_data})


def scrap(request):

    url = 'https://www.uhlbd.com/consultant/departments/gastro-liver-centre'
    response = requests.get(url)

    if response.status_code == 200:

        soup = selenium(url)
        doctors_list = soup.find_all('div', {'class': 'promo-box-bg'})
        doctor_data = []

        for i in doctors_list:
            name = i.find('h4', {'class': 'inner-post-title'}).text.strip()
            degree = i.find(
                'p', {'class': 'inner-post-sub-title'}).text.strip()
            specialist = i.find(
                'h4', {'class': 'inner-post-cont-title'}).text.strip()
            image_path = i.find(
                'div', {'class': 'promo-box-left'}).find('img').get('src')

            doctor_data.append({
                'name': name,
                'degree': degree,
                'specialist': specialist,
                'image_path': 'https://www.uhlbd.com/' + image_path,
                'hospital': 'UNITED HOSPITAL'

            })
        insert_doctors(doctor_data)
        return JsonResponse({'doctors': doctor_data})
    else:
        return HttpResponse(f"Failed to fetch data. Status code: {response.status_code}")


def selenium(url, browser='chrome'):
    # Configure headless mode for the chosen browser
    if browser.lower() == 'chrome':
        options = ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError('Invalid browser specified')

    driver.get(url)

    # Scroll to the bottom of the page
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the dynamic content to load
        time.sleep(2)

        # button = driver.find_element_by_xpath(
        #     "//img[@alt='close']")
        # # button = driver.find_element_by_id('js--notification-btn-close')

        # # Click the button
        # button.click()

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the dynamic HTML content
    html = driver.page_source

    # Close the browser window
    driver.quit()

    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def insert_doctors(doctors):

    for i in doctors:
        name = i.get('name')
        degree = i.get('degree')
        specialist = i.get('specialist')
        image_path = i.get('image_path', '')

        Doctor.objects.update_or_create(
            name=name,
            defaults={
                'degree': degree,
                'specialist': specialist,
                'image_path': image_path,
                'hospital': "UNITED HOSPITAL"
            }
        )


def scrape_doctorsSquare(request):

    url = 'https://www.squarehospital.com/doctors/department/UROLOGY'
    response = requests.get(url)

    if response.status_code == 200:

        soup = selenium(url)
        doctors_list = soup.find_all('div', {'class': 'docItem'})
        # print(book_list)
        # return HttpResponse(book_list)
        doctor_data = []

        for i in doctors_list:
            name = i.find('div', {'class': 'contentBox'}
                          ).find('h3').text.strip()
            specialist = i.find(
                'p').text.strip()
            image_path = i.find(
                'div', {'class': 'imgDiv'}).find('img').get('src')

            doctor_data.append({
                'name': name,
                'degree': '',
                'specialist': specialist,
                'image_path': image_path,
                'hospital': "SQUARE HOSPITAL"

            })
        insert_doctors(doctor_data)
        return JsonResponse({'doctors': doctor_data})
    else:
        return HttpResponse(f"Failed to fetch data. Status code: {response.status_code}")
