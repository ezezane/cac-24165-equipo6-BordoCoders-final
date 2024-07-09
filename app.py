from flask import Flask, render_template, request, redirect, flash, url_for
from db_crud import *
# secure_filename permite realizar una limpieza en el nombre del archivo
from werkzeug.utils import secure_filename

# imports
import os
import time

# carpeta donde se guardarán los archivos cargados por el CRUD
UPLOAD_FOLDER = 'static/img/uploads/'
# extensiones aceptadas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# creación y configuración de app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# función para verificar la extensión aceptada
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# función para generar el nombre del archivo que se subirá
# se usa el timestamp + el nombre original para evitar nombres duplicados
def filename_with_timestamp(filename):
    filename = secure_filename(filename)
    ts = round(time.time() * 1000)
    filename = str(ts) + "_" + filename
    return filename

# ---------------------
# PÁGINAS DEL FRONT-END
# ---------------------

# HOME
@app.route("/")
def cargar_home():
    title = 'Home | Perfumería Borbocoders'
    productosD = ProductosDestacados()
    return render_template("frontend/index2.html",title=title,productosD=productosD)


# SOBRE NOSOTROS
@app.route("/nosotros")
def cargar_nosotros():
    title = 'Sobre nosotros | Perfumería Borbocoders'
    return render_template("frontend/nosotros.html",title=title)


# CONTACTO
@app.route("/contacto")
def cargar_contacto():
    title = 'Quiero ser revendedor | Perfumería Borbocoders'
    return render_template("frontend/contact.html",title=title)


# LISTADO DE PRODUCTOS DB
@app.route("/productos")
def cargar_productos():
    title = 'Productos | Perfumería Borbocoders'
    productos = ReadProductos()
    return render_template("frontend/productos_db2.html",title=title,productos=productos)


# --------------------
# PÁGINAS DEL BACK-END
# --------------------


# HOME / LISTADO DE PRODUCTOS CARGADOS
# LISTADO DE PRODUCTOS DB
@app.route("/admin/")
def cargar_productos_admin():
    title = 'CRUD | Perfumería Borbocoders'
    productos = ReadProductos()
    return render_template("/backend/productos_db.html",title=title,productos=productos)


# CREAR NUEVO PRODUCTO -> método IMG
# documentación https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
# paso 1 FORM
@app.route("/admin/crear")
def crear_productos_img_admin():
    title = 'Create | Perfumería Borbocoders'
    return render_template("/backend/form_create_img.html",title=title)

# paso 2 CREAR
@app.route("/cargar_producto_img", methods=['POST'])
def crear_productos_img_db():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('no llegó ninguna imagen en el alta')
            return redirect(request.referrer)
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.referrer)
        
        # si los checkeos son válidos
        if file and allowed_file(file.filename):
            filename = filename_with_timestamp(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            prod_marca = request.form['marca']
            prod_name = request.form['name']
            prod_precio = request.form['precio']
            prod_URLimg = filename
            result = CreateDB(prod_marca,prod_name,prod_precio,prod_URLimg)

            #mensaje = '<div class="alert alert-success"><p>Se creó correctamente el producto</p></div>'
            return redirect("/admin/")
            #return redirect(url_for("/admin/", mensaje=mensaje))
            #return redirect(url_for('/admin/', mensaje=mensaje))



# EDITAR PRODUCTO
# paso 1 FORM precargado
@app.route("/admin/editar/<int:id>")
def editar_productos_img_form(id):
    productoID = ReadOneProduct(id)
    title = 'Update | Perfumería Borbocoders'
    return render_template("/backend/form_update_img.html",title=title,producto=productoID)

# paso 2 EDITAR
@app.route("/editar_producto_img", methods=['POST'])
def editar_productos_img_db():
    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == '':
            file_uploaded = False
        else:
            file_uploaded = True
            file = request.files['file']
            if allowed_file(file.filename):
                filename = filename_with_timestamp(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                prod_URLimg = filename
            else:
                return redirect(request.referrer)
        
        prod_id = request.form['prod_id']
        prod_marca = request.form['marca']
        prod_name = request.form['name']
        prod_precio = request.form['precio']
        
        if not file_uploaded:
            UpdateDB(prod_marca, prod_name, prod_precio, prod_id)
        else:
            UpdateDBIMG(prod_marca, prod_name, prod_precio, prod_URLimg, prod_id)
        
        return redirect("/admin/")
        
        
        
        
        
        # file = request.files['file']
        
        # # si los checkeos son válidos
        # if file and allowed_file(file.filename):
        #     filename = filename_with_timestamp(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #     prod_id = request.form['prod_id']
        #     prod_marca = request.form['marca']
        #     prod_name = request.form['name']
        #     prod_precio = request.form['precio']
        #     prod_URLimg = filename

        #     if prod_URLimg == "":
        #         # la imagen no se modifico
        #         conexion = conectarMySQL()
        #         with conexion.cursor() as cursor:
        #             result = UpdateDB(prod_marca,prod_name,prod_precio,prod_id)
        #         conexion.commit()
        #         conexion.close()
        #     else:
        #         # la imagen se modificó
        #         result = UpdateDBIMG(prod_marca,prod_name,prod_precio,prod_URLimg,prod_id)
        #     return redirect("/admin/")



# ELIMINAR PRODUCTO
# paso 1 FORM precargado
@app.route('/admin/borrar_producto/<int:id>')
def borrar_productos_img_form(id):
    productoID = ReadOneProduct(id)
    title = 'Delete | Perfumería Borbocoders'
    return render_template("/backend/form_delete_img.html",title=title,producto=productoID)

# paso 2 BORRAR
@app.route("/eliminar_producto/<int:id>", methods=['POST'])
def borrar_productos_img_db(id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    #mensaje = '<div class="alert alert-danger"><p>Se eliminó correctamente el producto</p></div>'
    return redirect("/admin/")






# *********************************************************************
# MÉTODO ORIGINAL V1
# CRUD CON URL DE IMAGEN
# *********************************************************************

# CREAR NUEVO PRODUCTO
# paso 1 FORM
@app.route("/admin/crear2")
def crear_productos_admin():
    title = 'Create | Perfumería Borbocoders'
    return render_template("/backend/form_create.html",title=title)

# paso 2 CREAR
@app.route("/cargar_producto", methods=['POST'])
def crear_productos_db():
    #print(request.form)
    prod_marca = request.form['marca']
    prod_name = request.form['name']
    prod_precio = request.form['precio']
    prod_URLimg = request.form['imgURL']
    result = CreateDB(prod_marca,prod_name,prod_precio,prod_URLimg)
    print(result)
    return redirect("/admin/")


# EDITAR PRODUCTO
# paso 1 FORM precargado
@app.route("/admin/editar2/<int:id>")
def editar_productos_form(id):
    productoID = ReadOneProduct(id)
    title = 'Update | Perfumería Borbocoders'
    return render_template("/backend/form_update.html",title=title,producto=productoID)

# paso 2 EDITAR
@app.route("/editar_producto", methods=['POST'])
def editar_productos_db():
    prod_id = request.form['prod_id']
    prod_marca = request.form['marca']
    prod_name = request.form['name']
    prod_precio = request.form['precio']
    prod_URLimg = request.form['imgURL']
    result = UpdateDB(prod_marca,prod_name,prod_precio,prod_URLimg,prod_id)
    print(result)
    return redirect("/admin/")


# ELIMINAR PRODUCTO
# paso 1 FORM precargado
@app.route('/admin/borrar_producto2/<int:id>')
def borrar_productos_form(id):
    productoID = ReadOneProduct(id)
    title = 'Delete | Perfumería Borbocoders'
    return render_template("/backend/form_delete.html",title=title,producto=productoID)

# paso 2 BORRAR
@app.route("/eliminar_producto2/<int:id>", methods=['POST'])
def borrar_productos_db(id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return redirect("/admin/")