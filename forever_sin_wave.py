#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys
import math
import time
import matplotlib.pyplot as plt
import datetime
dt = datetime.datetime.now()
import datetime


if __name__ == '__main__':

    # elements
    list_x = []
    list_y = []
    t = 0
    ph_ini = 0

    # plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    lines, = ax1.plot(list_x, list_y, marker='d',             # マーカーの形状
                      markersize=4,           # マーカー全体のサイズ
                      markerfacecolor='#66DDDD',  # マーカーの色は白
                      markeredgewidth=1,      # マーカーエッジのサイズ
                      markeredgecolor='#44BBBB',  # マーカーエッジを赤にする
                      linestyle='None')

    while True:
        x = t
        y = math.sin(x  + ph_ini )

        # print(x, y)

        list_x.append(x)
        list_y.append(y)

        # next step
        if t < 10:
            t += 0.1
        else:
            # plt
            lines.set_data(list_x, list_y)
            ax1.set_xlim(min(list_x), max(list_x))
            ax1.set_ylim(-1,1)
            plt.pause(0.5)

            # reset
            dt = datetime.datetime.now()
            dt = dt.strftime('%M%S')
            dt = (int(dt) % 100) / 10
            ph_ini = random.gauss(mu=0, sigma=0.3)
            print(ph_ini)

            t = 0
            list_x.clear
            list_y.clear
            time.sleep(0.5)


