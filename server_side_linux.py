#!/usr/bin/python3
#before using this script we need to create the file History.db in the folder C:\Users\USER\AppData\Roaming\Mozilla\Firefox\Profiles\u0zaow6i.default-release-1634662814557
#just do sqlite3 History.db
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import CPlib_linux as lib
import time,sqlite3,ast
from datetime import datetime

#if getattr(sys, 'frozen', False):
#    template_folder = os.path.join(sys._MEIPASS, 'templates')
#    static_folder = os.path.join(sys._MEIPASS, 'static')
#    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
#else:
#    app = Flask(__name__)

embranchement = lib.test_if_ext_exist()

if(embranchement == 1):
    app = Flask(__name__)
    @app.route('/akjksHBJJ56qsS:$skjs61SS2xcxcdf46SD$.',methods=['GET','POST'])
    @cross_origin(methods=['POST'])
    def get_time():
        actual_state = str(request.get_json())
        try:
            dict_actual_state = ast.literal_eval(actual_state)
        except Exception as e:
            print("datas are not kepts")
        path = lib.path_firefox_history(embranchement)
        path_to_sql_database = path[0]
        print(path_to_sql_database)
        localtime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        try:
            for key in dict_actual_state.keys():
                con = sqlite3.connect(path_to_sql_database)#if try doesn't work then there is no such database
                cur = con.cursor()
                sqlite_test_key_query = f"""SELECT EXISTS(SELECT 1 FROM visits WHERE url = '{key}') """#if we get one then there is an url so we have just to update otherwise we have to insert the new element.
                pings = cur.execute(sqlite_test_key_query).fetchall()[0][0]
                cur.close()
                if(pings == 1):#update (when there is a set url we keep visit-date the same changing visit_duration and url)
                    cur = con.cursor()
                    sqlite_update_query = f""" UPDATE visits SET visit_duration = {dict_actual_state[key]}
                    WHERE url = '{key}'
                    """
                    cur.execute(sqlite_update_query)
                else:
                    cur = con.cursor()
                    sqlite_insert_query = f"""INSERT INTO
                    visits(visit_date,visit_duration,url)
                    VALUES
                    ('{localtime}',{dict_actual_state[key]},'{key}')
                    """
                    cur.execute(sqlite_insert_query)
                con.commit()
                cur.close()
        except Exception as ex:
            print("an exception occur ", ex)
        return 'OK',200

    if __name__ =='__main__':
        app.run(debug = True,host = '127.0.0.1')
