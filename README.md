# nlp-tools
Some efficient tools for nlp task

【注】：本项目旨在：（1）记录一些平时常用的NLP工具类代码，避免重复造轮子，也方便交流使用；（2）记录一些常用方法的高效实现，便于交流探讨；

# 0.环境要求
* python 3.6 <br>
* 其他详见requirements.txt

# 1. 各任务详述
## 1.1 向量相似度的矩阵实现
代码文件：[matrix_similarity.py](https://github.com/lzhenboy/nlp-tools/blob/master/matrix_similarity.py) <br>
功能介绍：利用矩阵乘法实现向量间cos相似度的计算，可以大大提高计算效率，比循环计算法约提高几百倍（不同量级的相似度计算所提高的效率亦不同，向量维度越高，数目越多往往越明显），节省运行时间； <br>
功能示例：详见代码文件 [matrix_similarity.py](https://github.com/lzhenboy/nlp-tools/blob/master/matrix_similarity.py) <br>

