import random

if __name__ == '__main__':
    score = random.randint(0, 100)
    if score >= 60:
        print(score, 'Pass')
    else:
        print(score, 'Fail')

    print(score, 'Fail' if score < 60 else 'Pass')
