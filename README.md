# Huggingface Transformer Services

### To run locally:

#### Build docker Image

docker build -t huggingface-services .

#### Download models

mkdir -p models

docker run --rm -v $PWD/models:/models  -v   $PWD:/scripts -v $PWD/summarizer_config:/summarizer_config huggingface-services python  /scripts/get_models.py
#### Run docker

docker run --rm --name huggingface-services -v $PWD/models:/models -p 6500:5000 huggingface-services

To run swagger, open http://localhost:6500/transformers/ui/
