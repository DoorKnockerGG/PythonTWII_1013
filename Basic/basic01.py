if __name__ == '__main__':  #避免因用此當按時會執行程式
    high = 175
    weight = 92
    print(high, weight)
    print(type(high), type(weight))

    bmi = weight / ((high/100)**2)
    print('BMI=',bmi)
    print('BMI= ' + str(bmi))
    print('BMI= %.2f ' % bmi)
    print('bmi= {}'.format(bmi))
    print(f'bmi= {bmi}')