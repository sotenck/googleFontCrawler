# Google Font hosted to local

Automatic Web crawler for extracting and preparing google fonts for local use. This is nessessary due to european data protection law. (DSGVO) Downloading and linking all font-files by hand is tidious. So I wrote a small python script to automate the process.

When accessing google fonts over the "fonts.googleapis.com" url, the file is generated shortly after the request. Thus a webcrawler is needed to access the font-data at runtime.
## Requirments

- Firefox browser
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

__After that you will be able to access all nessessary files within the ```export```-folder__ 

All fonts will be downloaded to the ```fonts```-folder. Besides that, a ```header.html``` aswell as a ```font.css```-file is generated.

The ```font.css```-file looks something like this:

```
/* CORMORANT GARAMOND | latin-ext */
/* italic-700 */
@font-face{
	font-family: 'Cormorant Garamond';
	font-style: italic;
	font-weight: 700;
	src: url('../src/fonts/Cormorant-Garamond-italic-700-latin-ext.woff2') format('woff2');
	unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* normal-700 */
@font-face{
	font-family: 'Cormorant Garamond';
	font-style: normal;
	font-weight: 700;
	...

```

### What to do with output

1. Put the newly generated ```fonts```-folder into the ```src```-folder of your main project root. If you don't have an ```src```-folder, just create a new one. You could also manually adjust the paths of all fonts ```src```-attributes in the ```font.css```-file aswell as the ```header.html```-file.


2. Place the  ```font.css```-file into the ```css```-folder of your main project root. If you want to use another folder of your project, just adjust the path of the last line in ```header.html```

3. Copy the contents of ```header.html``` into the header section of every site you want to use the fonts on. 
Your code should look something like this:
	```
	<html>
		<header>

		<title>My website</title>
		...

		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Cormorant-Garamond-italic-700-latin-ext.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Cormorant-Garamond-normal-700-latin-ext.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Cormorant-Garamond-italic-700-latin.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Cormorant-Garamond-normal-700-latin.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Nunito-Sans-normal-400-latin-ext.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Nunito-Sans-normal-700-latin-ext.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Nunito-Sans-normal-900-latin-ext.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Nunito-Sans-normal-400-latin.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Nunito-Sans-normal-700-latin.woff2" crossorigin="anonymous" />
		<link as="font" rel="preload" type="font/woff2" href="./src/fonts/Nunito-Sans-normal-900-latin.woff2" crossorigin="anonymous" />
		<link rel="preload stylesheet" as="style" href="./css/font.css"  />
		...
	```

## Roadmap
Whats yet to implement
- Selection / Autodetection what browser to use for crawling
- Promp user to select which font character sets are to be exported.
__!! Currently only Latin and Latin-ext are beeing used !!__ 
- Promt user input for project paths of style-files and fonts-folder
