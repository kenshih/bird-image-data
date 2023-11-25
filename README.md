
# discovery

```
cat data/house_finch.female.100.json | jq -r '.[10:20] | .[].link'
```

# setup
```
python -m venv finchenv
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install --upgrade pip
```

# resources
* https://jqlang.github.io/jq/