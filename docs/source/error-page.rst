错误页面
==========
``AioWeRoBot`` 自带了一个错误页面，它将会在 Signature 验证不通过的时候返回错误页面。

定制错误页面
------------
如果你想为 ``AioWeRoBot`` 指定 Signature 验证不通过时显示的错误页面，可以这么做: ::

    @robot.error_page
    def make_error_page(url):
        return "<h1> %s </h1>" % url
