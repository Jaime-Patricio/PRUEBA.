# Importar
from flask import Flask, render_template


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')

# La segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# La tercera página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )


# La Cuarta página
@app.route('/<size>/<lights>/<device>')
def electronics(size, lights, device):
    return render_template(
                            'room.html',
                            size = size, 
                            lights = lights,
                            device = device
                            )

# Cálculo
@app.route('/<size>/<lights>/<device>/<room>')
def end(size, lights, device, room):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device),
                                                    int(room)
                                                    )
                        )
app.run(debug=True)
