import json
import boto3

textract = boto3.client("textract")
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("ResumeAnalysis")


def lambda_handler(event, context):

    bucket = event["bucket"]
    key = event["key"]

    response = textract.detect_document_text(
        Document={
            "S3Object": {
                "Bucket": bucket,
                "Name": key
            }
        }
    )

    extracted_text = ""

    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            extracted_text += item["Text"] + "\n"

    table.put_item(
        Item={
            "resumeId": key,
            "analysis": extracted_text
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            "Resume processed successfully"
        )
    }
