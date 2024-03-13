# ChestDiseaseClassification-CNN-Model

 - [Data link](https://drive.google.com/file/d/1hsiimUCC_-4dOfpy5diA1J2Tlr1QxMuO/view?usp=sharing)

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml 

## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -p .chest python=3.10 -y
```

```bash
conda activate .\.chest
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

## Mlflow Dagshub connection uri

``` bash
MLFLOW_TRACKING_URI=https://dagshub.com/sa-1-2/MLFLOW_EXPERIMENAT_DEMO.mlflow \
MLFLOW_TRACKING_USERNAME=sa-1-2 \
MLFLOW_TRACKING_PASSWORD=509dfe53ebe0c3edee59d0f2303119b789ab2018 \
python script.py
```

## Run from terminal

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/sa-1-2/MLFLOW_EXPERIMENAT_DEMO.mlflow

export MLFLOW_TRACKING_USERNAME=sa-1-2 

export MLFLOW_TRACKING_PASSWORD=509dfe53ebe0c3edee59d0f2303119b789ab2018

```