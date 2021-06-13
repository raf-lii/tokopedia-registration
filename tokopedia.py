#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

print("[+] Memulai Proses...")

driver = webdriver.Firefox() #Inisialisasi variable untuk mengakses browser firefox
driver.set_window_size(500, 500) # setting ukuran browser ke ukuran 500 x 500

print("[+] Mencoba Mengakses Link")
driver.get("https://www.tokopedia.com/register?ld=https%3A%2F%2Fwww.tokopedia.com%2F") #Memulai proses akses url

email = input("[~] Masukkan Email : ")
driver.find_element(By.ID, "regis-input").send_keys(email + Keys.ENTER) #Menemukan element berdasarkan ID

driver.implicitly_wait(10) #Delay 10 detik untuk memastikan halaman sudah terload secara sempurna
driver.find_element(By.CSS_SELECTOR, ".css-ti28tv-unf-btn").click() #Mengclick tombol konfirmasi

print("[+] Mencoba Mengirim Email...")
driver.implicitly_wait(10) #Delay 10 detik untuk memastikan halaman sudah terload secara sempurna
driver.find_element(By.CSS_SELECTOR, ".css-19d2cr0-unf-card").click() #Melakukan pengiriman email

otp = input("[~] Masukkan OTP : ")

print("[+] Memvalidasi OTP!")
driver.find_element(By.CSS_SELECTOR, ".css-11ic2m2").send_keys(otp + Keys.ENTER) #Mengirim OTP yang telah diinput user

print("[+] Mengisi Informasi Pribadi")
driver.find_element(By.ID, "regis-fullname").send_keys("Auto reg bot" + Keys.ENTER) #Mengirim Nama lengkap
driver.find_element(By.ID, "regis-password").send_keys("testingbro909" + Keys.ENTER) #Mengirim password

print("[+] Mencoba Login!")
driver.find_element(By.CSS_SELECTOR, ".css-gofphh-unf-btn").click() #Berhasil register

