# _*_coding:utf-8 _*_
# @Author　 : Ric
"""使用blueprint管理路由
"""
from flask import Blueprint

route_course = Blueprint('course_page', __name__)


@route_course.route('/')
def course():
    return 'Course Page'


@route_course.route('/python')
def course_python():
    return 'Python'
