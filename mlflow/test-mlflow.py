from mlflow import log_metric, log_param, log_artifact, set_experiment, create_experiment

if __name__ == "__main__":
    log_param("threshold", 3)
    log_param("verbosity", "DEBUG")

    log_metric("timestamp", 10000)
    

    log_artifact("produced_data.csv")
                 
