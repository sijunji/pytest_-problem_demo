
import time

import pytest


# pytest.report_title = '中文浏览器环境'
# pytest.browser_language = 'zh,zh_CN'
# report_name = 'test_No.' + str(int(time.time() * 1000)) + '.html'
# main_data = ['-v', '--html=static/report/' + report_name, 'step_page/test_prod_PC_demo.py::test_demo1',
#              'step_page/test_prod_PC_demo.py::test_demo']
# pytest.main(main_data)
#
#
import requests

session = requests.session()
data = {
    'data_list': [
        ['test_prod_PC_demo.py', [['test_demo1', 'test_demo2']]],
        # ['test_prod_PC_demo.py', [['test_demo1']]]
    ]
}

r = session.post('http://127.0.0.1:5005/run_ui_auto', json=data)
print(r.text)

