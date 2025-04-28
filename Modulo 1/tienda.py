from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos simulada
tiendas = [
    {"id": 1, "nombre": "Electrodomésticos XYZ", "categoria": "electrónica"},
    {"id": 2, "nombre": "Librería del Barrio", "categoria": "libros"},
    {"id": 3, "nombre": "Supermercado ABC", "categoria": "alimentación"}
]

# Ruta principal
@app.route('/')
def inicio():
    return """
    <h1>Directorio de Tiendas</h1>
    <ul>
        <li><a href="/tiendas">Ver todas las tiendas</a></li>
        <li><a href="/categorias">Ver categorías</a></li>
        <li><a href="/buscar">Buscar tienda</a></li>
        <li><a href="/about">Acerca de</a></li>
    </ul>
    """

# Mostrar todas las tiendas
@app.route('/tiendas')
def listar_tiendas():
    lista_html = "<h1>Nuestras Tiendas</h1><ul>"
    for tienda in tiendas:
        lista_html += f'<li><a href="/tienda/{tienda["id"]}">{tienda["nombre"]}</a></li>'
    lista_html += "</ul><a href='/'>Volver al inicio</a>"
    return lista_html

# Mostrar detalles de una tienda específica usando parámetros en la URL
@app.route('/tienda/<int:tienda_id>')
def detalle_tienda(tienda_id):
    for tienda in tiendas:
        if tienda["id"] == tienda_id:
            return f"""
            <h1>{tienda['nombre']}</h1>
            <p>Categoría: {tienda['categoria']}</p>
            <a href='/tiendas'>Volver a la lista</a>
            """
    return "Tienda no encontrada", 404

# Mostrar tiendas por categoría con parámetro opcional
@app.route('/categorias')
@app.route('/categorias/<categoria>')
def por_categoria(categoria=None):
    if categoria is None:
        # Mostrar lista de categorías disponibles
        categorias = set(tienda["categoria"] for tienda in tiendas)
        html = "<h1>Categorías</h1><ul>"
        for cat in categorias:
            html += f'<li><a href="/categorias/{cat}">{cat}</a></li>'
        html += "</ul><a href='/'>Volver al inicio</a>"
        return html
    else:
        # Mostrar tiendas de esa categoría
        tiendas_filtradas = [t for t in tiendas if t["categoria"] == categoria]
        if not tiendas_filtradas:
            return f"No hay tiendas en la categoría: {categoria}", 404
        
        html = f"<h1>Tiendas de {categoria}</h1><ul>"
        for tienda in tiendas_filtradas:
            html += f'<li><a href="/tienda/{tienda["id"]}">{tienda["nombre"]}</a></li>'
        html += "</ul><a href='/categorias'>Volver a categorías</a>"
        return html

# Ruta con diferentes métodos HTTP
@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        termino = request.form.get('termino', '')
        resultados = [t for t in tiendas if termino.lower() in t['nombre'].lower()]
        
        html = f"<h1>Resultados para: {termino}</h1>"
        if resultados:
            html += "<ul>"
            for tienda in resultados:
                html += f'<li><a href="/tienda/{tienda["id"]}">{tienda["nombre"]}</a></li>'
            html += "</ul>"
        else:
            html += "<p>No se encontraron resultados</p>"
        
        html += """
        <form action="/buscar" method="post">
            <input type="text" name="termino" placeholder="Buscar tiendas...">
            <button type="submit">Buscar</button>
        </form>
        <a href='/'>Volver al inicio</a>
        """
        return html
    else:
        return """
        <h1>Buscar Tiendas</h1>
        <form action="/buscar" method="post">
            <input type="text" name="termino" placeholder="Buscar tiendas...">
            <button type="submit">Buscar</button>
        </form>
        <a href='/'>Volver al inicio</a>
        """

# Página acerca de
@app.route('/about')
def about():
    return """
    <h1>Acerca de</h1>
    <p>Este es un directorio de tiendas de ejemplo creado con Flask.</p>
    <a href='/'>Volver al inicio</a>
    """

# Manejo de error 404 personalizado
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return """
    <h1>¡Página no encontrada!</h1>
    <p>Lo sentimos, la página que buscas no existe.</p>
    <a href='/'>Volver al inicio</a>
    """, 404

if __name__ == '__main__':
    app.run(debug=True)