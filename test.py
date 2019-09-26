# _*_coding:utf-8 _*_
# @Author　 : Ric
"""Flask 路由配置
    1.app.route('路由')
    2.app.route('/<username>')参数传递路由
    3.蓝牙注册（推荐，更好管理路由）

"""
from flask import Flask, url_for
from blue_print import route_course
from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
# 注册buleprint，url_prefix 添加前缀，方便将一类进行管理
app.register_blueprint(route_course, url_prefix='/course')
# mysql 服务下的mysql数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/mysql'
db = SQLAlchemy(app)


@app.route('/')
def hello():
    # 获取对应方法名的url
    url = url_for('index')
    # 自定义类管理url
    url1 = UrlManager.build_rul('/api')
    # 打印日志
    app.logger.info(url)
    sql = text('select * from user ')
    # sql = text('show tables')
    result = db.engine.execute(sql)
    for i in result:
        app.logger.info(i)
    return 'hello world' + url + url1


@app.route('/<username>')
def name(username):
    return username


@app.route('/index')
def index():
    return 'Index'


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return 'This page does not exist', 404


if __name__ == "__main__":
    # host允许公网访问
    # debug=True开启调试模式，自动检查代码变更和重启flask服务
    # threaded 开启多线程
    app.run(host='0.0.0.0', debug=True, threaded=True)
