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

Used Wiki Dump
==============
enwiki 20191101

References
==========
Wiki Extractor: version 2.75
https://github.com/attardi/wikiextractor
http://medialab.di.unipi.it/wiki/Wikipedia_Extractor

Wikipedia license: 
https://dumps.wikimedia.org/legal.html