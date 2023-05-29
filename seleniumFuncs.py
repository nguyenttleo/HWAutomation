from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import credentials as creds


def submitHW():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://classroom.google.com")

    search = driver.find_element_by_xpath('//*[@id="gfe-main-content"]/section[1]/div/div/div/ul/li[2]/a')

    search.click()

    time.sleep(1)

    driver.switch_to.window(window_name=driver.window_handles[0])
    driver.close()

    driver.switch_to.window(window_name=driver.window_handles[0])
    signin1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierId"]')))
    signin1.send_keys(creds.get_user())
    signin1.send_keys(Keys.RETURN)

    signin2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    signin2.send_keys(creds.get_pass())
    signin2.send_keys(Keys.RETURN)

    calcClass = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]')))
    calcClass.click()

    r = open("assignmentname.txt", "r")
    newest = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "' + r.read() + '")]')))
    newest.click()

    add = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Add or create")]')))
    add.click()

    addFile = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[13]/div/div/span[3]')))
    addFile.click()

    time.sleep(1)

    driver.switch_to.frame(3)

    inputFile = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/div')

    inputFile.click()
    time.sleep(0.5)
    r = open("assignmentname.txt", "r")
    # saves a backup copy
    pyautogui.write("HWImages")
    pyautogui.press('enter')
    time.sleep(0.5)
    # attaches homework file to assignment
    pyautogui.write(r.read() + ".pdf")
    pyautogui.press('enter')

    time.sleep(15)
    # submit assignment
    submit = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[3]/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[3]/div[3]/div')))
    submit.click()

    submit2 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[13]/div/div[2]/div[3]/div[2]')))
    submit2.click()

    time.sleep(3)
    comment = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '// *[ @ id = "yDmH0d"] / div[4] / div[3] / div[1] / div[2] / div[2] / div[4] / div[2] / div / div[2] / div[2]')))
    comment.click()

    time.sleep(2)

    pyautogui.write('Submitted by HWBot! :)')

    commentSubmit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '// *[ @ id = "yDmH0d"] / div[4] / div[3] / div[1] / div[2] / div[2] / div[4] / div[2] / div / div[4] / div / div[2] / div[2] / div')))
    commentSubmit.click()

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    submitHW()
