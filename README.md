Used Wiki Dump
==============
enwiki 20191101

Statistics
==========

Number of articles: 5828932 ~ 5.8M
Total tokens: 3088136411 ~ 3B
Unique tokens: 13578723 ~ 13M
Total words (alphabetical - no numbers, no non-english character): 2372584983 ~ 2.37B 
Unique words: 6068043 ~ 6M 
Total english words (checked with enchant dict): 2321090349 ~ 2.32B 
Unique english words (checked with enchant dict): 2096257 ~ 2M

Steps
=====
Parse wiki dump to text using wiki extractor:

```
python wikiextractor/WikiExtractor.py  wikidump/enwiki-20191101-pages-articles-multistream.xml \
        --json \
        --processes 4 \
        --templates parsed/templates \
        --output ./parsed \
        --bytes 2M \
        --sections \
        --lists \
        --min_text_length 0 \
        --filter_disambig_pages
```

output:

```
INFO: Finished 3-process extraction of 5828932 articles in 267726.0s (21.8 art/s)
INFO: total of page: 10469833, total of articl page: 5963484; total of used articl page: 5828932
```

References
==========
Wiki Extractor: version 2.75
https://github.com/attardi/wikiextractor
http://medialab.di.unipi.it/wiki/Wikipedia_Extractor

Wikipedia license: 
https://dumps.wikimedia.org/legal.html