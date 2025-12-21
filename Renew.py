from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Open TTVMA web app
driver.get("https://staging.ttvma.com/login")  

# Login (replace with credentials)
driver.find_element(By.ID, "username").send_keys("qa_user")
driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
driver.find_element(By.ID, "loginBtn").click()

# ------------------------------
# 1. Navigate to Operations / Services -> Renew DL
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Operations"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Renew DL"))).click()

# 2. Search & select Citizen
driver.find_element(By.ID, "searchCitizen").send_keys("Ali Mzayhem")
driver.find_element(By.ID, "searchBtn").click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr[data-id='citizenRow']"))).click()

# 3. Verify Citizen Info
assert driver.find_element(By.ID, "firstName").get_attribute("value") == "Ali"
assert driver.find_element(By.ID, "lastName").get_attribute("value") == "Mzayhem"

# 4. View licenses & select one for renewal
licenses = driver.find_elements(By.CLASS_NAME, "licenseRow")
licenses[0].find_element(By.CLASS_NAME, "selectLicense").click()

# 5. Select supporting documents (if any)
docs = ["idCopy", "photo", "currentLicense"]
for doc_id in docs:
    driver.find_element(By.ID, doc_id).click()

# 6. View Fees
fee_amount = driver.find_element(By.ID, "feeAmount").text
assert fee_amount in ["5,700,000", "4,600,000"], "Fee amount incorrect"

# 7. Click Save
driver.find_element(By.ID, "saveBtn").click()

# 8. Approve Application and Mark Paid
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Application Manager"))).click()
app_row = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-id='renewDL']")))
app_row.find_element(By.CLASS_NAME, "approveBtn").click()
app_row.find_element(By.CLASS_NAME, "markPaidBtn").click()

# ------------------------------
# Verify Enrollment Request (if applicable)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Enrollment"))).click()
enrollment_row = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-id='renewDL']")))
assert enrollment_row is not None, "Enrollment request not found"

# ------------------------------
# Close WebDriver
driver.quit()
