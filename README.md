Steps
=====
Parse wiki dump to text using wiki extractor:
```
python WikiExtractor.py -o parsed -b 5M --templates parsed/templates --processes 2 wikidump/enwiki-20191101-pages-articles-multistream.xml
```

output:
```
INFO: Finished 2-process extraction of 5963484 articles in 300744.7s (19.8 art/s)
INFO: total of page: 10469833, total of articl page: 5963484; total of used articl page: 5963484
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