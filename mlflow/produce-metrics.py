from mlflow  import log_metric
from random import choice

# metric_names = ["f1_score"]

percentages = [i for i in range(0, 100)]

for i in range(400):
    log_metric("f1_score", choice(percentages))
    