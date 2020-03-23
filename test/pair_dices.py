from random import randint
from pprint import pprint, pformat

def do_exp(times):
    exps_results = []
    for i in range(times):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        exps_results.append((dice1, dice2))
    return exps_results

def count(experiments):
    counts = {}
    for result in experiments:
        if result not in counts:
            counts[result] = 1
        else:
            counts[result] = counts[result] + 1
    return counts

if __name__ == '__main__':
    # pprint(pformat(count(do_exp(7))))
    print("\n".join("{}\t{}".format(k, v) for k, v in count(do_exp(51)).items()))