def get_min_max_score(*args):
    return min(args), max(args)
def get_average(**kwargs): 
    return (sum(kwargs.values())/len(kwargs)) 