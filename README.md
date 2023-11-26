# bird-image-data

Create bird image data set in order to train image recognition models

# history

- used in https://www.kaggle.com/code/kestrelken/bird-3-female-finch-images

# discovery/notes

```
# looking at data
cat data/house_finch.female.100.json | jq -r '.[10:20] | .[].link'

# zip data set
!zip -r out.zip ./*
```

# setup
```
python -m venv finchenv
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install --upgrade pip
# todo requirements.txt

# dev
source finchenv/bin/activate
source secrets
```

# resources
* https://jqlang.github.io/jq/