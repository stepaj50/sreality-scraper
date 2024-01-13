from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text
from crawler import crawl
import psycopg2

from http_server import run_server

if __name__ == '__main__':

    results = crawl()

    engine = create_engine("postgresql://postgres:12345678@db:5432")
    db = scoped_session(sessionmaker(bind=engine))
    if engine.dialect.has_table(engine.connect(), table_name="sreality"):
        db.execute(text("DROP TABLE sreality;"))
    db.execute(text("CREATE TABLE sreality (title TEXT, img_url TEXT);"))

    for item in results:
        db.execute(text("INSERT INTO sreality (title, img_url) VALUES ('{title}','{img_url}');".format(title=item["title"],img_url=item["img_url"])))
    db.commit()
    db.close()

    run_server()
