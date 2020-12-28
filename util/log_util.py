#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import datetime

filename = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
# print('filename = ', filename)

# 设置日志格式
logging.basicConfig(level=logging.INFO, # 日志级别
                    format= '%(asctime)s ' # 格式化日志内容
                            '%(name)s:%(levelname)s [%(filename)s:%(lineno)d] '
                            ': %(message)s ',
                    datefmt='%Y-%m-%d %H:%M:%S', # 日期格式
                    # filename=filename # 日志文件
                    )

# 创建logger对象
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('this is a info log')
    logger.warning('this is a warning log')