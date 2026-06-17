# adaptive_network_policy.py
import requests
from kubernetes import client, config
from kubernetes.client.rest import ApiException

class AdaptiveNetworkPolicy:
    def __init__(self):
        config.load_incluster_config()
        self.v1 = client.NetworkingV1Api()
    
    def get_workload_risk_score(self, namespace, workload):
        # Query risk scoring service (e.g., Falco, Sysdig)
        risk_api = "http://risk-scorer.default.svc.cluster.local/api/v1/risk"
        response = requests.get(f"{risk_api}/{namespace}/{workload}")
        return response.json().get('risk_score', 0.5)
    
    def enforce_adaptive_policy(self, namespace, workload):
        risk_score = self.get_workload_risk_score(namespace, workload)
        
        policy_spec = {
            "apiVersion": "networking.k8s.io/v1",
            "kind": "NetworkPolicy",
            "metadata": {"name": f"adaptive-{workload}"},
            "spec": {
                "podSelector": {"matchLabels": {"app": workload}},
                "policyTypes": ["Ingress", "Egress"]
            }
        }
        
        # High risk: Deny all except monitoring
        if risk_score > 0.8:
            policy_spec['spec']['ingress'] = [{
                "from": [{"namespaceSelector": {"matchLabels": {"name": "monitoring"}}}]
            }]
            policy_spec['spec']['egress'] = [{"to": [{"namespaceSelector": {"matchLabels": {"name": "internet"}}]}]
        
        # Medium risk: Allow internal traffic only
        elif risk_score > 0.5:
            policy_spec['spec']['ingress'] = [{"from": [{"namespaceSelector": {"matchLabels": {"kubernetes.io/metadata.name": namespace}}}]}]
        
        # Low risk: Default permissive
        else:
            policy_spec['spec']['ingress'] = [{"from": []}]
        
        try:
            self.v1.replace_namespaced_network_policy(f"adaptive-{workload}", namespace, policy_spec)
            print(f"Applied adaptive policy for {workload}: risk={risk_score}")
        except ApiException as e:
            print(f"Policy update failed: {e}")

# Usage
controller = AdaptiveNetworkPolicy()
controller.enforce_adaptive_policy("genai-prod", "llm-inference")
