# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 11:45
# @Author  : lzhenboy
import time

import numpy as np


class Similarity(object):
    def __init__(self):
        pass

    def sim_by_matmul(self, vec_mat1, vec_mat2):
        '''
        Cal the similarity by matmul, which has high computational efficiency
        :param vec_mat1: vector-matrix1 -> (m, k)
        :param vec_mat2: vector-matrix2 -> (n, k)
        :return: sim -> (m, n)
        '''

        # Transfer format for input
        vec_mat1 = np.array(vec_mat1)
        vec_mat2 = np.array(vec_mat2)

        # Dot product
        vec_dots = np.matmul(vec_mat1, vec_mat2.transpose())

        # Norm of vectors
        vec_mat1_norm_ = np.sqrt(np.sum(vec_mat1 ** 2, axis=1))
        vec_mat2_norm_ = np.sqrt(np.sum(vec_mat2 ** 2, axis=1))
        vec_mat1_norm = np.reshape(vec_mat1_norm_, (vec_mat1_norm_.shape[0], -1))
        vec_mat2_norm = np.reshape(vec_mat2_norm_, (vec_mat2_norm_.shape[0], -1))
        vec_norms = np.matmul(vec_mat1_norm, vec_mat2_norm.transpose())

        # Cal similarity
        similarity = vec_dots / vec_norms
        return similarity

    def sim_by_loop(self, vec_mat1, vec_mat2):
        '''
        Cal the similarity by loop, which has low computational efficiency
        :param vec_mat1: vector-matrix1 -> (m, k)
        :param vec_mat2: vector-matrix2 -> (n, k)
        :return: sim -> (m, n)
        '''
        similarity_ = []
        for vec1 in vec_mat1:
            vec1_ = np.reshape(np.array(vec1), (len(vec1),))
            vec1_norm = np.sqrt(np.sum(vec1_ ** 2))
            s_ = []
            for vec2 in vec_mat2:
                vec2_ = np.reshape(np.array(vec2), (len(vec2),))
                vec2_norm = np.sqrt(np.sum(vec2_ ** 2))
                v_dot = np.matmul(vec1_, vec2_.transpose())
                v_norm = vec1_norm * vec2_norm
                s_.append(v_dot / v_norm)
            similarity_.append(s_)
        return similarity_


if __name__ == '__main__':
    # Prepare Data
    vec_dim = 200
    vec1 = [list(np.random.rand(vec_dim)) for _ in range(3000)]
    vec2 = [list(np.random.rand(vec_dim)) for _ in range(5000)]

    # Compute Similarity
    sim = Similarity()

    start_time = time.time()
    sim_mat = sim.sim_by_matmul(vec1, vec2)
    print('Running time of sim_by_matmul is: {:.4f}s'.format(time.time() - start_time))
    start_time = time.time()
    sim_mat_ = sim.sim_by_loop(vec1, vec2)
    print('Running time of sim_by_loop is: {:.4f}s'.format(time.time() - start_time))
