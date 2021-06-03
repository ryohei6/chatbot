how to set env:

```bash
pip install -r requirements.txt
python -m spacy dowmload ja_core_news_md
```


how to train:

```bash
rasa train
```

how to start server:

```bash
python -m rasa_core_sdk.endpoint --actions actions
```

how to start shell:

```bash
rasa shell# chatbot
```
