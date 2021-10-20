import math

if __name__ == '__main__':
    r = 123
    # 求圓面積 ＆球體積 （利用math api 取得圓周率）
    # 結果印出小數點到第二位
    area = math.pow(r, 2) * math.pi
    volume = 4/3 * math.pi * math.pow(r, 3)
    print('area= %.2f' % area)
    print('volume= %.2f' % volume)
    # 若要加上千分位
    print(area, type(area))
    print('%.2f' % area, type('%.2f' % area))
    print(format(float('%.2f' % area), ","))
