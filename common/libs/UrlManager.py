# _*_coding:utf-8 _*_
# @Author　 : Ric


class UrlManager(object):
    """
    url链接管理器
    """
    @staticmethod
    def build_rul(path):
        return path

    @staticmethod
    def build_static_utl(path):
        """添加版本信息"""
        path = path + '?version=' + '20190909'
        return UrlManager.build_rul(path)
