#-*-coding:utf-8-*-
import json
from os import path
from io import open
import sys
import nltk
import traceback
from nltk.tag.stanford import POSTagger
nltk.internals.config_java("C:/Program Files/Java/jre7/bin/java.exe", options='-Xmx8g')
reload(sys)
sys.setdefaultencoding("utf-8")

# load
st = POSTagger(path.realpath('stanford-postagger/models/english-bidirectional-distsim.tagger'), path.realpath('stanford-postagger/stanford-postagger-3.4.jar'), encoding='utf8')
file_path = path.relpath("data/introAfterRevision.txt")
# tag
intro = []
tags = {}
with open(file_path, 'r', encoding='utf8') as a:
    count = -1
    for line in a:
        if not line.strip():
            # empty line
            count += 1
            intro.append("")
            a.next()
        else:
            intro[count] += line
with open('log.txt', 'w', encoding='utf-8') as b:
    for index, value in enumerate(intro):
        initialIndex = 0
        if index <= initialIndex:
            continue
        print index
        tags[index] = []
        try:
            tags[index].extend(st.tag(unicode(value).split()))
        except Exception:
            b.write('Error in: \t' + unicode(index)+'\n' + unicode(traceback.format_exc()))
            b.flush()
        if index % 100 == 0 and index != initialIndex:
            file_name = unicode(index - 100) + '.json'
            f = open(file_name, 'w', encoding='utf-8')
            f.write(unicode(json.dumps(tags, ensure_ascii=False, indent=4)))
            f.close()
            tags = {}