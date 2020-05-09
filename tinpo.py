from random import shuffle
tinpo = 'ちんぽ'
result = ''
while not result.endswith((tinpo,)):
    result += shuffle(tinpo)

print(result)