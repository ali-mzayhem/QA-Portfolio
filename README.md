# QA Case Study – TTVMA Vehicle Registration System

## Project Overview
- Organization: Traffic, Truck & Vehicle Management Authority (TTVMA)
- System Type: Government Web-Based System
- Domain: Vehicle Registration & Licensing
- Role: QA Engineer
- Testing Type: Manual & Automated Testing
- Environment: Test / Staging

## System Description
The TTVMA system manages vehicle registration, driving exams, licensing workflows, and citizen records.  
The system is mission-critical and requires high accuracy, data integrity, and process reliability.

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

## Test Approach
- Requirement-based testing from functional specifications
- End-to-end testing of user flows
- Risk-based testing for high-impact modules
- Exploratory testing to uncover edge cases
- Cross-browser testing (Chrome, Edge)
- Automated regression testing using Selenium with Python
- Automated API testing using Postman / Newman for backend verification

## Test Artifacts
- 📋 [Manual Test Cases & Scenarios](https://docs.google.com/document/d/1obBYg-6bmxsXW05WEku2Z7R_r_DquGhnboqCt_j0A9E/edit?usp=drive_link)
- 🐞 [Bug Reports – Jira Style]([https://docs.google.com/spreadsheets/d/1N0UNluPKfuGABzAiERWwAnW2OD1mKbVmq3zWGuOAJ8Q/edit?usp=drive_link](https://drive.google.com/file/d/1mSridHYOo0GmmkCdbp7iWQWhTHFzae3Q/view?usp=sharing))
- 🤖 Sample Automation Scripts (Python/Selenium) [Link to Scripts](https://github.com/YOUR_GITHUB_REPO/ttvma-automation)

## Sample Defects Identified
- Citizen records not appearing in reports before theoretical exam
- Inconsistent status updates between exam request and results modules
- Validation errors during practical exam result submission
- Missing error handling for invalid request states

## Risk & Impact Analysis
- Prevented incorrect exam status assignments
- Reduced risk of invalid driving license issuance
- Improved reliability of reporting and audit data
- Increased system confidence before release
- Automated regression scripts reduced manual testing effort by ~30%

## Collaboration & Communication
- Worked closely with backend developers to reproduce defects
- Verified fixes through regression testing
- Communicated findings clearly using structured bug reports
- Supported system validation prior to deployment
- Shared automated scripts with QA team to improve testing efficiency

## Conclusion
This case study demonstrates my ability to test complex, high-responsibility systems with a focus on accuracy, risk reduction, real-world usability, and automation—essential for government and enterprise environments.
