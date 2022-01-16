#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from typing import List


class PSquare:
    """
    Python implementation of the p square algo from this paper: https://www1.cse.wustl.edu/~jain/papers/ftp/psqr.pdf
    The aim of p square is to estimate the p quantile of a distribution without storing data. Every time a new
    value is drawn from the distribution p square updates its estimates.
    This algo is particularly valuable when you work on online models and want to iteratively know a quantile, say
    the median or the 95 percentile to build your own confidence
    """

    def __init__(self, p):
        """
        Initiate p square models with the p value to estimate and five first observations
        :param p: the percentile to iteratively estimate
        """
        p = p / 100.0
        self.initiated = False
        self.marker_heights = []
        self.marker_positions = [i for i in range(1, 6)]  # marker positions are 1-based
        self.desired_positions = [1.0, 1.0 + 2.0 * p, 1.0 + 4.0 * p, 3.0 + 2.0 * p, 5.0]
        self.increments = [0.0, p / 2.0, p, (1.0 + p) / 2.0, 1.0]

    def find_cell(self, new_observation):
        """
        Find the higher marker whose height is lower than observation.
        Return -1 if observation is lower than any known marker heigth
        :param new_observation: new observation, numeric value
        :return: index of the higher marker whose height is lower than observation. Return -1 if obs is lower
        than any marker height
        """
        if new_observation < self.marker_heights[0]:
            return -1
        i = 0
        while i + 1 < len(self.marker_heights) and (new_observation >= self.marker_heights[i + 1]):
            i = i + 1
        return i

    def _parabolic(self, i, d):
        """
        Parabolic formula for updating marker heights
        :param i: index of the marker height to update
        :param d: sign of (position - desired position)
        :return: new value for marker height at index i
        """
        term1 = d / float(self.marker_positions[i + 1] - self.marker_positions[i - 1])

        term2 = (self.marker_positions[i] - self.marker_positions[i - 1] + d) * \
                (self.marker_heights[i + 1] - self.marker_heights[i]) / \
                float(self.marker_positions[i + 1] - self.marker_positions[i])

        term3 = (self.marker_positions[i + 1] - self.marker_positions[i] - d) * \
                (self.marker_heights[i] - self.marker_heights[i - 1]) / \
                float(self.marker_positions[i] - self.marker_positions[i - 1])

        return self.marker_heights[i] + term1 * (term2 + term3)

    def _linear(self, i, d):
        """
        Linear formula for updating marker heights
        :param i: index of the marker height to update
        :param d: sign of (position - desired position)
        :return: new value for marker height at index i
        """
        return self.marker_heights[i] + d * \
               (self.marker_heights[i + d] - self.marker_heights[i]) / \
               float(self.marker_positions[i + d] - self.marker_positions[i])

    def update(self, new_observation):
        """
        Step B.1 and B.2 in the paper algo
        Find cell k containing new observation and update current and desired marker positions
        :param new_observation: a new observation (numeric value)
        """
        if not self.initiated:
            self.marker_heights.append(new_observation)
            if len(self.marker_heights) == 5:
                self.initiated = True
                self.marker_heights.sort()
            else:
                return

        i = self.find_cell(new_observation)
        if i == -1:
            self.marker_heights[0] = new_observation
            k = 0
        elif i == 4:
            self.marker_heights[4] = new_observation
            k = 3
        else:
            k = i

        # self.marker_positions[k + 1:] = self.marker_positions[k + 1:] + 1
        for i in range(k + 1, len(self.marker_positions)):
            self.marker_positions[i] += 1
        # self.desired_positions = self.desired_positions + self.increments
        for i in range(len(self.increments)):
            self.desired_positions[i] += self.increments[i]
        self.adjust_height_values()

    def adjust_height_values(self):
        """
        Step B.3 in the paper algo
        Adjust height values using either parabolic or linear formula
        """
        for i in range(1, 4):
            d = self.desired_positions[i] - self.marker_positions[i]
            if (d >= 1 and (self.marker_positions[i + 1] - self.marker_positions[i]) > 1) or \
                    (d <= -1 and (self.marker_positions[i - 1] - self.marker_positions[i]) < -1):

                d = -1 if d < 0 else 1

                qprime = self._parabolic(i, d)
                if self.marker_heights[i - 1] < qprime < self.marker_heights[i + 1]:
                    self.marker_heights[i] = qprime

                else:
                    qprime = self._linear(i, d)
                    self.marker_heights[i] = qprime

                self.marker_positions[i] += d

    def p_estimate(self):
        """
        :return: current estimation of quantile p, NaN if not enough information
        """
        if len(self.marker_heights) > 2:
            return self.marker_heights[2]
        else:
            return None


if __name__ == '__main__':
    NB_ITERATIONS = 30000
    import time
    from random import random

    values = [random() for _ in range(5)]
    quantile_to_estimate = 50  # this vault is equal to median

    psquare = PSquare(quantile_to_estimate)
    exact_quantiles = []
    estimated_quantiles = []
    psquare_exec_time = []
    numpy_exec_time = []

    for val in values:  # p square algorithm necessitates 5 values to start
        psquare.update(val)


    def get_median(arr: List):
        """from statistics import median"""
        arr.sort()
        mid = len(arr) >> 1
        return arr[mid] if len(arr) % 2 == 1 else (arr[mid] + arr[mid - 1]) / 2


    for _ in range(NB_ITERATIONS):
        new_val = random()
        values.append(new_val)

        psquare_start = time.time()
        psquare.update(new_val)
        estimated_quantiles.append(psquare.p_estimate())
        psquare_end = time.time()

        numpy_start = time.time()
        exact_quantiles.append(get_median(values))
        numpy_end = time.time()

        psquare_exec_time.append(psquare_end - psquare_start)
        numpy_exec_time.append(numpy_end - numpy_start)
    for i in range(len(estimated_quantiles)):
        print(
            f'estimated={estimated_quantiles[i]} exact={exact_quantiles[i]} time_diff={psquare_exec_time[i] - numpy_exec_time[i]}')
