
# Google Font hosted to local

Automatic Web crawler for extracting and preparing google fonts for local use.

## Requirments

- python > __3.6__
- python pip packages:
    - selenium
    - geckodriver-autoinstaller
    - requests

## Usage

Start the system cli in main folder of this repo and run following command:
```
python getGoogleFonts.py
```

After that, find the old Google-Font include link. It should look something like this:

```
<html>
    <header>

    <title>My website</title>
    ...

    <link href="https://fonts.googleapis.com/css?family=Cormorant+Garamond:700,700i|Nunito+Sans:400,700,900" rel="stylesheet">

...
```

Enter just the url itself into the python cli promt:

```
Please copy your Google® fonts include URL here:

https://fonts.googleapis.com/css?family=Cormorant+Garamond:700,700i|Nunito+Sans:400,700,900
```

After that you will be able to access all nessessary files within the ```export```-Folder