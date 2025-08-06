# You are building a grid search over a set of model parameters. 
# Given a dictionary where keys are parameter names and values are 
# lists of options, return all combinations of parameters using itertools.product.

from itertools import product 

def params_finer(input_dict):
    keys = input_dict.keys()
    values = input_dict.values()

    combinations = list(product(*values))
    results = [dict(zip(keys, combo)) for combo in combinations]
    return results

def main():

    params = {
        "learning_rate": [0.1, 0.01],
        "batch_size": [16, 32],
    }

    res = params_finer(params)
    for r in res:
        print(r)
if __name__ == '__main__':
    main()