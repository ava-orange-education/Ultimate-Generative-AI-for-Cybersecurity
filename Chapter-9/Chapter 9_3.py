from elasticsearch import Elasticsearch

es = Elasticsearch(["your-elastic-host"])
job_id = "your_anomaly_job"
result = es.ml.estimate_model_memory(job_id=job_id)
print(result)
