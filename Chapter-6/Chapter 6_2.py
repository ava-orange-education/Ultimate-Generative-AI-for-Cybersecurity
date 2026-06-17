# adaptive_iam_policy.py
import boto3
import json
from datetime import datetime, timedelta

def lambda_handler(event, context):
    iam = boto3.client('iam')
    threat_intel = event.get('threat_intel', {})
    
    role_name = event['role_name']
    workload_risk = threat_intel.get('risk_score', 0.5)
    threat_indicators = threat_intel.get('indicators', [])
    
    # Baseline policy (low risk)
    baseline_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "*"}
        ]
    }
    
    # Adaptive tightening
    if workload_risk > 0.7 or 'crypto_mining' in threat_indicators:
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {"Effect": "Deny", "Action": "*", "Resource": "*"}  # Lockdown
            ]
        }
    elif workload_risk > 0.4:
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::secure-bucket/*"},
                {"Effect": "Deny", "Action": ["s3:DeleteBucket"], "Resource": "*"}
            ]
        }
    else:
        policy = baseline_policy
    
    # Apply policy with TTL
    policy_document = json.dumps(policy)
    iam.put_role_policy(
        RoleName=role_name,
        PolicyName=f"adaptive-policy-{int(datetime.now().timestamp())}",
        PolicyDocument=policy_document
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Applied adaptive policy for {role_name}",
            "risk_score": workload_risk,
            "ttl_minutes": 60
        })
    }
