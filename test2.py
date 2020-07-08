import os
from pyltp import Segmentor
 
 
LTP_DATA_DIR = r'D:\ModelFiles\LTP\ltp_data_v3.4.0'   # LTP模型目录路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径， 模型名称为'cws.model'
 
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
words = segmentor.segment('元芳你怎么看')  # 分词
print(type(words))
print(type('|'.join(words)))
print('|'.join(words))
segmentor.release()   # 释放模型
