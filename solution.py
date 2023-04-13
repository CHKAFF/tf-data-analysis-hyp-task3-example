import numpy as np
from scipy.stats import ttest_ind


chat_id = 303247798

def solution(control_sample, test_sample) -> bool:
    t_statistic, p_value = ttest_ind(control_sample, test_sample)
    alpha = 0.01
    return p_value < alpha
