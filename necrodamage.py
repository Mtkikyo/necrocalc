from decimal import *
def damagecalc(damage, dicead, cost, times = 0, cut = 1, explode = 1, wide = 1, reroll = 'なし', additional = 0):
    number = 10
    result = {'total':0, 'max':0, 'min':0, 'average':0, 'dpc':0}
    extra = {'max':0, 'min':0, 'average':0}
    if (reroll == '大成功' and not dicead):
        return result
    for i in range(1,11):
        roll = i + dicead
        if (roll <= 5):
            if (reroll == 'なし'):
                atk = 0
                result['min'] = 0
            else:
                number -= 1
        else:
            atk = damage
            if (roll > 10):
                atk += (roll - 10)
            elif (reroll == '大成功'):
                number -= 1
                continue
            if additional:
                cost += additional['cost'] / 10
                atk += additional['add']
                atk *= (wide + additional['multi']) / wide
            atk *= (cut * explode * wide)
            if times:
                extra = damagecalc(damage, dicead, cost, times - 1, cut, explode, wide, reroll)
            if (i == 10):
                result['max'] = atk + extra['max']
            elif (i == 1):
                result['min'] = atk + extra['min']
            elif (reroll == '成功' and roll == 6):
                result['min'] = atk + extra['min']
            elif (reroll == '大成功' and roll == 11):
                result['min'] = atk + extra['min']
            result['total'] += (atk + extra['average'])
    result['average'] = Decimal(result['total']) / number
    result['dpc'] = result['average'] / cost
    return result