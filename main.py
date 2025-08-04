from flask import Flask, jsonify
import pyodbc
import pandas as pd

app = Flask(__name__)

@app.route('/api/despachospc', methods=['GET'])
def get_despachospc():
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=172.18.0.2;DATABASE=SCourier;UID=csantisteban;PWD=csantisteban'
    )
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql('SELECT * FROM dbo.DESPACHOSPC', conn)
    conn.close()

    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
