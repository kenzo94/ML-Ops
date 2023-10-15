# End to end ML Project

## Workflow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update dvc.yaml

# How to run?
### STEPS:

Clone the repository

```bash
https://https://github.com/kenzo94/ML-Ops
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
- mlflow ui


#### dagshub
[dagshub](https://dagshub.com)
MLFLOW_TRACKING_URI=https://dagshub.com/kenzo94/ML-Ops.mlflow \
MLFLOW_TRACKING_USERNAME=kenzo94 \
MLFLOW_TRACKING_PASSWORD=8753b04ed498c50f40388010fee24743d51213c5 \
python script.py

Run this to export as env variables
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/kenzo94/ML-Ops.mlflow 

export MLFLOW_TRACKING_USERNAME=kenzo94

export MLFLOW_TRACKING_PASSWORD=8753b04ed498c50f40388010fee24743d51213c5
```