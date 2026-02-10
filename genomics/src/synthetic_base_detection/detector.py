import re

def detect(seq: str):
    matches = re.findall(r'X{2,}Y{1,}Z', seq)
    return {"synthetic_bases": len(matches), "confidence": min(1.0, len(matches)/10)}

)}

