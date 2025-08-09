# Traitify Images

I applied to Taco Bell in January 2025.  I was given an assessment to complete where different pictures show up (each with a label).  And then I could answer with whether each matches my personality or now.  The image associations are interesting and humourous.  That's why I posted them here.

---

**[`assessments.json`](./assessments.json):** a manual concatenation of multiple GET calls to this URL (at different stages of my application process):

```
https://c-and-r-restaurant-grou.traitify.com/traitify-js/profiles/25925432-1f45-4d3d-8824-426bfbfcae94/assessments?apply_assessment_expiration=true&data=blend,recommendation,traits,types&image_pack=linear&locale_key=en-US
```

**[`download.py`](./download.py):** a script which scrapes `assessments.json` and saves whichever images come out into [`./Images`](./Images).
