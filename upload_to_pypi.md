# Update version number

# Upload

```bash
python -m pip install --upgrade setuptools wheel twine build
python -m pip install --upgrade build

# Remove old packages and update version number
rm -rf dist start_selenium_webdriver.egg-info

python -m build
python -m twine upload dist/*
```
