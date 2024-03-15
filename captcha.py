from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the Chrome Driver Path
chrome_driver_path = "C:\Program Files\drivers\chromedriver.exe"

# Create a ChromeService object
chrome_service = webdriver.chrome.service.Service(chrome_driver_path)

# Initialize Chrome driver with options and service
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("buster.crx")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# Koo App URL
page_url = "https://www.kooapp.com/"

# Navigate to the Koo App page
driver.get(page_url)

# Wait for some time for the page to load
time.sleep(2)

# Maximizing the window
driver.maximize_window()

# Click the login button
login_button = driver.find_element(By.CLASS_NAME, 'Header_loginBtn__gu5Jl')
login_button.click()

# Wait for the login modal to appear
time.sleep(2)

# Click the "Sign in with Email" button
try:
    sign_with_email = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[3]/div[3]/button[2]/span[2]')
except NoSuchElementException:
    sign_with_email = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div[3]/div[3]/button')
sign_with_email.click()

# Wait for the email input field to appear
time.sleep(2)

# Enter the email
email = 'nagasaigadupudi111@gmail.com'
email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys(email)

# Handle reCAPTCHA here (ensure you have the rights and permissions to do this)

# Wait for the OTP input field to appear
time.sleep(2)

# Enter the OTP
otp = input("Enter the OTP code: ")
otp_input = driver.find_element(By.XPATH, '//*[@id="otp"]')
otp_input.send_keys(otp)

# Click the verify button
verify_button = driver.find_element(By.CLASS_NAME, 'Login_verifyBtn__Hs7YX')
verify_button.click()

# Refresh the page
driver.refresh()

# Add any additional steps to complete the login process

# Close the browser when done
driver.quit()