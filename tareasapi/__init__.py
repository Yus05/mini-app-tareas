from flask import Flask, session, render_template, request, redirect, url_for

def create_app():

    app = Flask(__name__)
    
    # configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev'
    )
    
    @app.route('/')
    def index():
        return render_template('index.html')
        
    
    @app.route('/tareas')
    def tareas():
        if 'tareas' not in session:
            session['tareas'] = []
            
        lista_tareas = session['tareas']
        return render_template('tareas.html', tareas=lista_tareas)
    
    
    @app.route('/agregar', methods=['GET', 'POST'])
    def agregar():
        if request.method == 'POST':
            nueva_tarea = request.form.get('tarea', '').strip()
            
            if nueva_tarea:
                tareas = session.get('tareas', [])
                tareas.append(nueva_tarea)
                session['tareas'] = tareas  # REASIGNACIÓN explícita
            return redirect(url_for('tareas'))

        return render_template('agregar.html')   
    
    
    @app.route('/eliminar/<int:indice>', methods=['POST'])
    def eliminar(indice):
        tareas = session.get('tareas', [])
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            session['tareas'] = tareas
        return redirect(url_for('tareas'))

    
    return app



