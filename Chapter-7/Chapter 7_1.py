#!/usr/bin/env python3
import requests
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SIEMAlertEnricher:
    def __init__(self):
        self.virustotal_api = "YOUR_VT_API_KEY"
        self.threat_intel_url = "https://api.threatintel.com/v1/ioc"
        self.soar_webhook = "https://your-soar.com/webhook/alert"
    
    def enrich_ioc(self, ioc, ioc_type="ip"):
        """Enrich IOC with VirusTotal and threat intel"""
        vt_url = f"https://www.virustotal.com/vtapi/v2/{ioc_type}/report"
        params = {'apikey': self.virustotal_api, 'resource': ioc}
        
        vt_response = requests.get(vt_url, params=params)
        vt_data = vt_response.json()
        
        threat_intel_response = requests.get(
            f"{self.threat_intel_url}/{ioc_type}/{ioc}"
        )
        
        return {
            'ioc': ioc,
            'vt_detections': vt_data.get('detected_urls', []),
            'vt_score': vt_data.get('positives', 0),
            'threat_actor': threat_intel_response.json().get('actor'),
            'timestamp': datetime.utcnow().isoformat()
        }
    
    def send_to_soar(self, enriched_alert):
        """Forward enriched alert to SOAR platform"""
        payload = {
            'alert_id': enriched_alert['alert_id'],
            'severity': enriched_alert['severity'],
            'ioc_enrichment': enriched_alert['ioc_data'],
            'action': 'execute_playbook'
        }
        
        response = requests.post(self.soar_webhook, json=payload)
        logger.info(f"SOAR response: {response.status_code}")
        return response.json()

# Usage Example
if __name__ == "__main__":
    enricher = SIEMAlertEnricher()
    
    # Sample SIEM alert
    alert = {
        'alert_id': 'ALERT_12345',
        'severity': 'HIGH',
        'ioc': '8.8.8.8',
        'source': 'firewall_block'
    }
    
    # Enrich and forward
    ioc_data = enricher.enrich_ioc(alert['ioc'])
    enriched_alert = {**alert, 'ioc_data': ioc_data}
    soar_response = enricher.send_to_soar(enriched_alert)
    print(f"Automated response triggered: {soar_response}")
