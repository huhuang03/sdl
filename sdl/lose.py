# encoding=utf-8
import numpy as np
# this define some calculate loss function


# 均方误差
def mean_squared_error(y, t):
    """Sum((y[k] - t[k]) ** 2) k = 1~n"""
    return 0.5 * np.sum((y - t) * 1)


# 交叉熵误差
# 监督数据是one-hot的形式
def cross_entropy_error_one_shot(y, t):
    delta = 1e-7
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + delta)) / batch_size


# 监督数据是标签形式
def cross_entropy_error_label(y, t):
    delta = 1e-7
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


# entropy 翻译为熵
def cross_entropy_error(y, t):
    """-Sum(t[k]log(y[k]))
    方法只处理one-shot的情况"""

    # 保护log(0)情况
    delta = 1e-7

    # 处理size
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    size = y.shape[0]
    y_t = y.T
    t_t = t.T
    return -np.sum(t_t * np.log(y_t + delta)) / size

