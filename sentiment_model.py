from transformers import pipeline
#import tensorflow as tf


def analyze(text):
    sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
    data = text

    res = sentiment_pipeline(data)

    return res
