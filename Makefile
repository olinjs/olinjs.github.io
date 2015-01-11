index.html : jade/index.json jade/index.jade stylesheets/style.css
	jade jade/index.jade -O jade/index.json -o .

jade/index.json : jade/in.json get-img.py
	python get-img.py

stylesheets/style.css : stylus/style.styl
	stylus stylus/style.styl -o stylesheets