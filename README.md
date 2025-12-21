# QA Case Study – TTVMA Vehicle Registration System

## Project Overview
- **Organization:** Traffic, Truck & Vehicle Management Authority (TTVMA)  
- **System Type:** Government Web-Based System  
- **Domain:** Vehicle Registration & Licensing  
- **Role:** QA Engineer  
- **Testing Type:** Manual & Automated Testing  
- **Environment:** Test / Staging  

## System Description
The TTVMA system contains various applications, including the Driving License (DL) Web App for employees, the Vehicle Registration (VR) Web App, and a citizen-facing website and mobile app.  
The system is mission-critical and requires **high accuracy, data integrity, and process reliability**.  
The scope includes testing all software components from **end-to-end workflows**, covering citizen services, backend processes, and administrative interfaces.

## QA Objectives
- Validate critical vehicle registration workflows  
- Ensure data accuracy between frontend and backend  
- Detect functional and usability defects early  
- Reduce risks before deployment to production  
- Automate repetitive or high-risk test scenarios to save time and increase coverage  

## Testing Scope
- Citizen registration & profile management  
- Exam requests (theoretical & practical)  
- Exam results processing  
- Vehicle & license data handling  
- Admin & officer workflows  
- Dynamic fee validation and multi-license scenarios  

## Test Approach
- Requirement-based testing from functional specifications  
- End-to-end testing of user flows across all apps  
- Risk-based testing for high-impact modules  
- Exploratory testing to uncover edge cases  
- Cross-browser testing (Chrome, Edge)  
- Automated regression testing using Selenium with Python  
- Automated API testing using Postman / Newman for backend verification  

## Test Artifacts
- 📋 [Manual Test Cases & Scenarios](https://drive.google.com/file/d/1883FjEgdwTzujF9G0dx9xyDZdailXN7Z/view?usp=sharing)  
- 🐞 [Bug Reports – Jira Style](https://drive.google.com/file/d/1mSridHYOo0GmmkCdbp7iWQWhTHFzae3Q/view?usp=sharing)  
- 🤖 [Sample Automation Scripts](https://github.com/ali-mzayhem/QA-Portfolio/blob/main/AutomationScript.py)  

## Sample Defects & Risks Identified
These are **real-world issues discovered and tracked via Jira tickets** during testing:

- **Dynamic Fee Miscalculation:**  
  Some license categories (e.g., A1) had incorrect fees displayed compared to standard values (5,700,000 vs 4,600,000). Detected during category validation workflow.  

- **Multiple Exam Requests Handling:**  
  When citizens applied for multiple license types in foreign exchange, separate exam requests were not generated properly, leading to incorrect scheduling and reporting.  

- **Nationality Validation:**  
  System allowed non-Lebanese citizens to select restricted public vehicle categories, violating business rules.  

- **Age Restriction Enforcement:**  
  New DL creation allowed citizens under 18 or 21 (depending on category) to proceed, potentially bypassing legal requirements.  

- **Exam Status Sync Issues:**  
  Practical and theoretical exam statuses were sometimes not reflected in reports or enrollment pages immediately after completion.  

- **Re-approval Workflow Bug:**  
  Editing rejected applications and resubmitting could cause workflow inconsistencies, including missing exam requests or enrollment requests.  


These defects **prevented incorrect license issuance, ensured compliance with legal rules, and improved system reliability** prior to production deployment. Each was tracked in Jira with full reproduction steps, screenshots, and severity ratings.

## Risk & Impact Analysis
- Prevented incorrect exam status assignments  
- Reduced risk of invalid driving license issuance  
- Improved reliability of reporting and audit data  
- Increased system confidence before release  
- Automated regression scripts reduced manual testing effort by ~40%  

## Collaboration & Communication
- Worked closely with backend developers to reproduce defects  
- Verified fixes through regression testing  
- Communicated findings clearly using structured bug reports  
- Supported system validation prior to deployment  
- Shared automated scripts with QA team to improve testing efficiency  

## Conclusion
This case study demonstrates my ability to **test complex, high-responsibility systems** with a focus on **accuracy, risk reduction, real-world usability, and automation**—essential for government and enterprise environments.
