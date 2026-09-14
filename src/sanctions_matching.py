from difflib import SequenceMatcher
import re
def normalize_name(value):
    return re.sub(r'[^a-z0-9 ]','',str(value).lower()).strip()
def name_similarity(a,b):
    return round(100*SequenceMatcher(None,normalize_name(a),normalize_name(b)).ratio())
