#! /Users/michael/anaconda3/bin/python
# @Date:   2018-09-01 09:00:44

# 评分算法实现

# 基础天梯分数
R0 = 1400

def rating(Ra, Rb):
    """
    Ra: 赢的一方玩家 a 的分数
    Rb: 输的一方玩家 b 的分数
    """
    # K值，用于控制分数改变的幅度，数字越大幅度越大
    K = 16
    Sa = 1
    Sb = 0

    Ea = 1 / (1 + 10**((Ra - Rb)/400))
    Eb = 1 / (1 + 10**((Rb - Ra)/400))

    Ra = Ra + K * (Sa - Ea)
    Rb = Rb + K * (Sb - Eb)

    return Ra, Rb


if __name__ == '__main__':
    
    Ra = 1400
    Rb = 1400

    for i in range(100):
        Ra, Rb = rating(Ra, Rb, 1)
        print(Ra, Rb)




