from flask import Flask, render_template
import datetime, time, random
from threading import Thread, Event
import light_config as config 

sys_name = config.sys_name

#import opc
app = Flask(__name__)

settings = {
	'power' : False,
	'color' : 'Rainbow',
	'pattern': 'none',
	'pattern_running': False,
	'color_one': 'White',
	'color_two': 'White',
	'color_three': 'White',
	'hide_color_one': True,
	'hide_color_two': True,
	"hide_color_three": True,
}

@app.route("/")
def main():

	templateData = {
	'sys_name': sys_name,
	'settings': settings
	}
	return render_template('main.html', **templateData)

@app.route("/power/<action>")
def power(action):
	if action == "on":
		# update the dictionary 
		settings['power']=True

	if action == "off":
		# update the dictionary 
		settings['power']=False

	templateData = {
	'sys_name': sys_name,
	'settings' : settings
	}
	return render_template('main.html', **templateData)

@app.route("/start/Rainbow/<pattern>")
def start_rainbow(pattern):
	settings['color']='Rainbow'
	settings['pattern']=pattern
	settings['pattern_running']=True
	settings['hide_color_one']=True
	settings['hide_color_two']=True
	settings['hide_color_three']=True
	templateData = {
	'sys_name': sys_name,
	'settings' : settings
	}
	return render_template('main.html', **templateData)

@app.route("/start/Solid-Fade/<pattern>")
def start_solid_fade(pattern):
	settings['color']='Solid-Fade'
	settings['pattern']=pattern
	settings['pattern_running']=True
	settings['hide_color_one']=True
	settings['hide_color_two']=True
	settings['hide_color_three']=True
	templateData = {
	'sys_name': sys_name,
	'settings' : settings
	}
	return render_template('main.html', **templateData)

@app.route("/start/One-Color/<color1>/<pattern>")
def start_one_color(color1,pattern):
	settings['color']='One-Color'
	settings['color1']=color1
	settings['pattern']=pattern
	settings['pattern_running']=True
	settings['hide_color_one']=False
	settings['hide_color_two']=True
	settings['hide_color_three']=True
	templateData = {
	'sys_name': sys_name,
	'settings' : settings
	}
	return render_template('main.html', **templateData)

@app.route("/start/Two-Color/<color1>/<color2>/<pattern>")
def start_two_color(color1,color2,pattern):
	settings['color']='Two-Color'
	settings['color_one']=color1
	settings['color_two']=color2
	settings['pattern']=pattern
	settings['pattern_running']=True
	settings['hide_color_one']=False
	settings['hide_color_two']=False
	settings['hide_color_three']=True
	templateData = {
	'sys_name': sys_name,
	'settings' : settings
	}
	return render_template('main.html', **templateData)

@app.route("/start/Three-Color/<color1>/<color2>/<color3>/<pattern>")
def start_three_color(color1,color2,color3,pattern):
	settings['color']='Three-Color'
	settings['color_one']=color1
	settings['color_two']=color2
	settings['color_three']=color3
	settings['pattern']=pattern
	settings['pattern_running']=True
	settings['hide_color_one']=False
	settings['hide_color_two']=False
	settings['hide_color_three']=False
	templateData = {
	'sys_name': sys_name,
	'settings' : settings
	}
	return render_template('main.html', **templateData)

@app.route("/stop")
def stop():
	settings['pattern_running']=False
	templateData = {
	'sys_name': sys_name,
	'settings' : settings
	}
	return render_template('main.html', **templateData)

	

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)