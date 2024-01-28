#!/usr/bin/env python3
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if sentence else None)
