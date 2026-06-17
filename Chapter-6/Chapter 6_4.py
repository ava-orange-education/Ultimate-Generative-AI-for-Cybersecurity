# self-healing-genai.yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: self-healing-genai
spec:
  rules:
  - name: quarantine-high-risk-pods
    match:
      any:
      - resources:
          kinds:
          - Pod
          namespaces:
          - genai-prod
    validate:
      message: "High-risk pod quarantined"
      deny:
        conditions:
          all:
          - key: "{{ request.operation || 'CREATE' }}"
            operator: Equals
            value: CREATE
          - key: "{{ metadata.labels.risk_score || '0' }}"
            operator: GreaterThan
            value: "0.8"
    mutate:
      patchStrategicMerge:
        metadata:
          annotations:
            quarantine.revoke: "true"
        spec:
          containers:
          - name: "{{ metadata.name }}"
            resources:
              limits:
                cpu: "100m"
                memory: "128Mi"
