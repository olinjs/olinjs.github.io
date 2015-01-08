index : jade/index.json jade/index.jade style
	jade jade/index.jade -O jade/index.json -o .

img :
	python get-img.py

style : stylus/style.styl
	stylus stylus/style.styl -o stylesheets