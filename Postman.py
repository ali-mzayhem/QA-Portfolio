{
  "info": {
    "name": "TTVMA DL API",
    "_postman_id": "12345-abcde",
    "description": "API tests for TTVMA Vehicle Registration System",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Create New DL",
      "request": {
        "method": "POST",
        "header": [
          {"key": "Content-Type", "value": "application/json"}
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"firstName\": \"Ali\",\n  \"lastName\": \"Mzayhem\",\n  \"dob\": \"2005-12-21\",\n  \"nationality\": \"Lebanese\",\n  \"licenseCategory\": \"A1\",\n  \"documents\": [\"idCopy\",\"photo\",\"residencyProof\"],\n  \"fees\": 5700000\n}"
        },
        "url": {"raw": "https://staging.ttvma.com/api/newDL", "protocol": "https", "host": ["ttvma","example","com"], "path": ["api","newDL"]}
      },
      "response": []
    },
    {
      "name": "Renew DL",
      "request": {
        "method": "POST",
        "header": [
          {"key": "Content-Type", "value": "application/json"}
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"citizenId\": \"CIT123456\",\n  \"licenseId\": \"DL987654\",\n  \"documents\": [\"idCopy\",\"photo\",\"currentLicense\"],\n  \"fees\": 5700000\n}"
        },
        "url": {"raw": "https://staging.ttvma.com/api/renewDL", "protocol": "https", "host": ["ttvma","example","com"], "path": ["api","renewDL"]}
      },
      "response": []
    }
  ]
}
