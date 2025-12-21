from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Open TTVMA web app
driver.get("https://staging.ttvma.com/login")  # replace with actual URL

# Login (replace with credentials)
driver.find_element(By.ID, "username").send_keys("qa_user")
driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
driver.find_element(By.ID, "loginBtn").click()

# ------------------------------
# 1. Navigate to Services -> New DL
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Services"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create New DL"))).click()

# 2. Input Citizen Info
driver.find_element(By.ID, "firstName").send_keys("Ali")
driver.find_element(By.ID, "lastName").send_keys("Mzayhem")
driver.find_element(By.ID, "dob").send_keys("2005-12-21")  # 18+ validation
driver.find_element(By.ID, "nationality").send_keys("Lebanese")
driver.find_element(By.ID, "district").send_keys("Beirut")
driver.find_element(By.ID, "registrationNumber").send_keys("REG123456")

# 3. Parent Full Names
driver.find_element(By.ID, "fatherName").send_keys("Mohamed Mzayhem")
driver.find_element(By.ID, "motherName").send_keys("Fatima Mzayhem")

# 4. Choose License Category
driver.find_element(By.ID, "licenseCategory").send_keys("A1")  # e.g., private license
time.sleep(1)

# 5. Select Supporting Documents
docs = ["idCopy", "photo", "residencyProof"]
for doc_id in docs:
    driver.find_element(By.ID, doc_id).click()

# 6. Select Fees
driver.find_element(By.ID, "feeOption").click()  # default fee selection
fee_amount = driver.find_element(By.ID, "feeAmount").text
assert fee_amount in ["5,700,000", "4,600,000"], "Fee amount incorrect"

# 7. Click Save
driver.find_element(By.ID, "saveBtn").click()

# ------------------------------
# 8. Approve Application and Mark Paid
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Application Manager"))).click()
app_row = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-id='newDL']")))
app_row.find_element(By.CLASS_NAME, "approveBtn").click()
app_row.find_element(By.CLASS_NAME, "markPaidBtn").click()

# ------------------------------
# 9. Check Enrollment Request
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Enrollment"))).click()
enrollment_row = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-id='newDL']")))
assert enrollment_row is not None, "Enrollment request not found"

# 10. Check Driving Exam Request
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Exams"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Exam Requests"))).click()
exam_row = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-id='newDL']")))
assert exam_row is not None, "Exam request not found"

# 11. Take Exam (simulate score submission)
exam_row.find_element(By.CLASS_NAME, "takeExamBtn").click()
driver.find_element(By.ID, "practicalScore").send_keys("85")  # passing score
driver.find_element(By.ID, "submitExamBtn").click()

# ------------------------------
# 12. Verify Practical Exam Score in Reports
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Exam Reports"))).click()
report_row = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-id='newDL']")))
score = report_row.find_element(By.CLASS_NAME, "practicalScore").text
assert score == "85", "Practical exam score not saved correctly"

# ------------------------------
# Close WebDriver
driver.quit()
