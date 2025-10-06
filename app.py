from flask import Flask, render_template_string
import mysql.connector
import os

app = Flask(__name__)

# Plantilla HTML 
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Aplicación Docker</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        table { margin: auto; border-collapse: collapse; width: 60%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Registros de Usuarios</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Apellido</th>
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route('/')
def index():
    try:
        # conexión a la base de datos
        mydb = mysql.connector.connect(
          host=os.getenv("MYSQL_HOST"),
          user=os.getenv("MYSQL_USER"),
          password=os.getenv("MYSQL_ROOT_PASSWORD"),
          database=os.getenv("MYSQL_DATABASE")
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT id, nombre, apellido FROM usuarios")
        myresult = mycursor.fetchall()

        return render_template_string(HTML_TEMPLATE, data=myresult)

    except mysql.connector.Error as err:
        return f"Error de conexión a la base de datos: {err}"

    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)