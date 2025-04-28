# app.py
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_para_csrf'  # Necesaria para CSRF en formularios

# Nombres de los campos del formulario
texto_nombre = 'Nombre'
texto_email = 'Email'
texto_asunto = 'Asunto'
texto_mensaje = 'Mensaje'
texto_enviar = 'Enviar Mensaje'

# Definición del formulario con WTForms
class ContactForm(FlaskForm):
    nombre = StringField(texto_nombre, validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField(texto_email, validators=[DataRequired(), Email()])
    asunto = StringField(texto_asunto, validators=[DataRequired(), Length(min=2, max=100)])
    mensaje = TextAreaField(texto_mensaje, validators=[DataRequired(), Length(min=10, max=500)])
    enviar = SubmitField(texto_enviar)

# Lista para almacenar los mensajes (en un proyecto real usarías una base de datos)
mensajes = []

#Con el método GET: muestra el formulario de contacto
#Con el método POST: procesa los datos enviados, los valida y si son correctos:
    #Crea un diccionario con los datos
    #Lo añade a la lista de mensajes
    #Muestra mensaje de éxito
    #Redirige a la página de mensajes recibidos

@app.route('/', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        nuevo_mensaje = {
            'nombre': form.nombre.data,
            'email': form.email.data,
            'asunto': form.asunto.data,
            'mensaje': form.mensaje.data
        }
        mensajes.append(nuevo_mensaje)
        flash('¡Tu mensaje ha sido enviado correctamente!')
        # Reinicia el formulario después de enviar el mensaje
        form = ContactForm(formdata=None)

        # Redirige a la página de mensajes recibidos
        #return redirect(url_for('mensajes_recibidos'))
    
    # Si es GET o el formulario no es válido, se muestra la página con el formulario
    return render_template('contacto.html', form=form)

@app.route('/mensajes')
def mensajes_recibidos():
    return render_template('mensajes.html', mensajes=mensajes)

if __name__ == '__main__':
    app.run(debug=True)