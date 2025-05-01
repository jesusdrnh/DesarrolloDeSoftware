from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from datetime import datetime
from config import Config
from models import db, Task

def create_app(config_class=Config):
    """To-Do en Flask"""
    
    # Inicializar la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # OPERACIONES CRUD
    
    # READ - Mostrar todas las tareas (página principal)
    @app.route('/')
    def index():
        # Obtener filtros de la URL (si existen)
        status = request.args.get('status', 'all')
        priority = request.args.get('priority', 'all')
        
        # Iniciar la consulta
        query = Task.query
        
        # Aplicar filtros
        if status == 'pending':
            query = query.filter_by(done=False)
        elif status == 'completed':
            query = query.filter_by(done=True)
            
        if priority != 'all':
            query = query.filter_by(priority=int(priority))
            
        # Ordenar las tareas (primero las no completadas, luego por prioridad y fecha)
        tasks = query.order_by(Task.done, Task.priority.desc(), Task.due_date).all()
        
        return render_template('todo/index.html', tasks=tasks)
    
    # CREATE - Formulario para crear una nueva tarea
    @app.route('/tasks/create', methods=['GET', 'POST'])
    def create_task():
        if request.method == 'POST':
            # Obtener datos del formulario
            title = request.form.get('title', '').strip()
            description = request.form.get('description', '').strip()
            priority = int(request.form.get('priority', 1))
            due_date_str = request.form.get('due_date', '')
            
            # Validar datos
            errors = {}
            if not title:
                errors['title'] = ['El título es obligatorio']
            
            # Si hay errores, volver al formulario
            if errors:
                return render_template('todo/create.html', errors=errors)
            
            # Crear nueva tarea
            new_task = Task(
                title=title,
                description=description,
                priority=priority,
                done=False
            )
            
            # Procesar fecha de vencimiento si se proporciona
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                    new_task.due_date = due_date
                except ValueError:
                    # Si la fecha no es válida, simplemente no la establecemos
                    pass
            
            # Guardar en la base de datos
            db.session.add(new_task)
            db.session.commit()
            
            flash('Tarea creada con éxito', 'success')
            return redirect(url_for('index'))
        
        # GET - Mostrar formulario
        return render_template('todo/create.html')
    
    # UPDATE - Editar una tarea existente
    @app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
    def edit_task(task_id):
        # Obtener la tarea o devolver 404 si no existe
        task = Task.query.get_or_404(task_id)
        
        if request.method == 'POST':
            # Obtener datos del formulario
            title = request.form.get('title', '').strip()
            description = request.form.get('description', '').strip()
            priority = int(request.form.get('priority', 1))
            due_date_str = request.form.get('due_date', '')
            done = 'done' in request.form
            
            # Validar datos
            errors = {}
            if not title:
                errors['title'] = ['El título es obligatorio']
            
            # Si hay errores, volver al formulario
            if errors:
                return render_template('todo/edit.html', task=task, errors=errors)
            
            # Actualizar la tarea
            task.title = title
            task.description = description
            task.priority = priority
            task.done = done
            
            # Procesar fecha de vencimiento
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                    task.due_date = due_date
                except ValueError:
                    pass
            else:
                task.due_date = None
            
            # Guardar cambios
            db.session.commit()
            
            flash('Tarea actualizada con éxito', 'success')
            return redirect(url_for('index'))
        
        # GET - Mostrar formulario con datos actuales
        return render_template('todo/edit.html', task=task)
    
    # DELETE - Eliminar una tarea
    @app.route('/tasks/<int:task_id>/delete', methods=['POST'])
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        
        # Eliminar de la base de datos
        db.session.delete(task)
        db.session.commit()
        
        flash('Tarea eliminada con éxito', 'success')
        return redirect(url_for('index'))
    
    # UPDATE - Marcar/desmarcar tarea como completada
    @app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
    def toggle_task(task_id):
        task = Task.query.get_or_404(task_id)
        
        # Cambiar el estado
        task.done = not task.done
        db.session.commit()
        
        status_msg = "completada" if task.done else "pendiente"
        flash(f'Tarea marcada como {status_msg}', 'success')
        return redirect(url_for('index'))
    
    # Manejo de errores 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    return app

# Para ejecutar con flask run
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)