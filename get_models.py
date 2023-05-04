from transformers import pipeline, AutoTokenizer, AutoModelWithLMHead
import sys
import os
MODEL = '/models'
if len(sys.argv) > 1:
    MODEL = sys.argv[1]

MODEL_SUMM = MODEL + '/summarizer'

if not os.path.exists(MODEL_SUMM):
    os.mkdir(MODEL_SUMM,0o755)

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-xsum-12-6")
model = AutoModelWithLMHead.from_pretrained("sshleifer/distilbart-xsum-12-6")
summarizer_pipeline = pipeline("summarization", model=model,tokenizer=tokenizer)
try:
    summarizer_pipeline.save_pretrained(MODEL_SUMM)
except:
    pass
