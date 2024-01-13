from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text

hostName = "0.0.0.0"
serverPort = 8080

def get_results():

    engine = create_engine("postgresql://postgres:12345678@db:5432")
    db = scoped_session(sessionmaker(bind=engine))
    engine.connect()

    results = db.execute(text("SELECT * from sreality"))

    db.close()

    return results

    # db_hostname = 'db'
    # db_username = 'postgres'
    # db_password = '12345678'
    # db_port = '5432'
    #
    # connection = psycopg2.connect(host=db_hostname, user=db_username, password=db_password, port=db_port)
    #
    # cur = connection.cursor()
    #
    # cur.execute("""SELECT * from sreality""")
    #
    # return cur.fetchall()

class HttpServer(BaseHTTPRequestHandler):

    def do_GET(self):

        results = get_results()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body>", "utf-8"))
        for item in results:
            self.wfile.write(bytes(f'<div>{item[0]}', "utf-8"))
            self.wfile.write(bytes(f'<img src="{item[1]}">', "utf-8"))
            self.wfile.write(bytes("</div>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))



def run_server():

    webServer = HTTPServer((hostName, serverPort), HttpServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

if __name__ == "__main__":
    run_server()
