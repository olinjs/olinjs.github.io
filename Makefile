index.html : content/index.json jade/index.jade stylesheets/style.css
	jade jade/index.jade -O content/index.json -o .

content/index.json : content/input.json get-img.py
	python get-img.py

stylesheets/style.css : stylus/style.styl
	stylus stylus/style.styl -o stylesheets
