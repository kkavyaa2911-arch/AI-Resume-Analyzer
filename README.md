# AI Resume Analyzer

A serverless AI Resume Analyzer built using AWS Lambda, Amazon S3, Amazon Textract, DynamoDB, and Amazon Bedrock.

---

## Project Overview

This project automatically processes resumes uploaded to Amazon S3. It extracts text using Amazon Textract, stores the extracted data in DynamoDB, and is designed to use Amazon Bedrock for AI-powered resume analysis.

---

## Architecture

```
Resume PDF
     │
     ▼
Amazon S3
     │
     ▼
AWS Lambda
     │
     ▼
Amazon Textract
     │
     ▼
Amazon DynamoDB
     │
     ▼
Amazon Bedrock (AI Analysis)
```

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon Textract
- Amazon DynamoDB
- Amazon Bedrock (planned)
- IAM
- CloudWatch

---

## Project Workflow

1. Upload a resume PDF to Amazon S3.
2. AWS Lambda is triggered.
3. Amazon Textract extracts the resume text.
4. The extracted text is stored in DynamoDB.
5. Amazon Bedrock analyzes the resume (planned).

---

## S3 Configuration

- **Bucket Name:** `kavyaa-resume`
- **Region:** `ap-south-1`
- **Sample S3 URI:** `s3://kavyaa-resume/sample_resume.pdf`

> **Note:** For security, avoid publishing your personal resume or full object URLs in a public repository. Use a sample file name such as `sample_resume.pdf` in documentation.

---

## Technologies

- Python
- Boto3
- AWS Lambda
- Amazon S3
- Amazon Textract
- DynamoDB

---

## Current Status

- ✅ Resume Upload
- ✅ Text Extraction
- ✅ DynamoDB Storage
- ⏳ Amazon Bedrock Integration (Pending)

---

## Future Improvements

- AI Resume Scoring
- ATS Compatibility Analysis
- Skill Gap Detection
- Resume Improvement Suggestions
- Streamlit Web InterfaceoDB.
## Project Screenshots

### Amazon S3 Bucket
![S3 Bucket](screenshots/screenshots%20s3%20bucket.png)

### AWS Lambda Function
![Lambda Function](screenshots/Screenshot%20lambda.png)

### Lambda Test Output
![Lambda Test Output](screenshots/Screenshot%20lambda%20test%20output.png)

### Amazon DynamoDB
![DynamoDB](screenshots/Screenshot%20dynamo%20db.png)

### Amazon CloudWatch Logs
![CloudWatch Logs](screenshots/Screenshot%20watch%20log.png)
