#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence):
        size = len(sentence)
        lett = sentence[0]
        return((size, lett))
    return ((0, None))
