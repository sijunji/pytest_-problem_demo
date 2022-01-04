# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
import: pytest, flask, flask_cors
"""
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
import pytest
from flask import Flask, request, make_response
from flask_cors import *
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(__file__))


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)


app.executor = ThreadPoolExecutor(10)


def analytical_data(data, report_name):
    """
    将请求中的参数放入队列
    """
    pytest_run_data = ['-v', f'--html={report_name}']
    for i in data:

        if len(i) == 1:
            data_str = '' + i[0]
            pytest_run_data.append(data_str)
            continue
        else:
            data_str = '' + i[0] + '::'
            if issubclass(type(i[1][0]), list):
                for y in i[1][0]:
                    pytest_run_data.append(data_str + y)
                    continue
            elif len(i[1]) == 1:
                pytest_run_data.append(data_str + i[1][0])
                continue
            else:
                for y in i[1][1]:
                    pytest_run_data.append(data_str + i[1][0] + '::' + y)
    pytest.main(pytest_run_data)


@app.route('/run_ui_auto', methods=["POST"])
def run_ui_auto():
    """

    接口接收一个list
    [[test_file.py, [class_name, [model_name1, model_name2]]]]: 有类，有方法执行
    [[test_file.py, [[model_name1, model_name2]]]]: 没有类，指定方法执行
    [[test_file.py, []]]: 按照文件运行
    [
     [test_file.py, []],
     [test_file.py, [[model_name1, model_name2]]],
     [test_file.py, [类名, [model_name1, model_name2]]]
    ]: 多文件运行
    """
    report_key = str(int(time.time() * 1000))
    report_name = 'test_No.' + report_key + '.html'
    data_list = request.json.get('data_list')
    app.executor.submit(analytical_data, data_list, report_name)

    return make_response({'msg': 'running.....', 'report_key': report_key})



if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5005, threaded=False)
