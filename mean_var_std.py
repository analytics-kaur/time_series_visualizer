import numpy as np
print(np.__version__)

def calculate(list):
    if len(list)!=9:
        raise ValueError('list must contain 9 numbers')
    else:
        mat=np.array(list).reshape(3,3)
        mean=[(mat.mean(axis=0).tolist()),(mat.mean(axis=1).tolist()),(mat.flatten().mean())]
        var=[(mat.var(axis=0).tolist()),(mat.var(axis=1).tolist()),(mat.flatten().var())]
        std=[(mat.std(axis=0).tolist()),(mat.std(axis=1).tolist()),(mat.flatten().std())]
        max=[(mat.max(axis=0).tolist()),(mat.max(axis=1).tolist()),(mat.flatten().max())]
        min=[(mat.min(axis=0).tolist()),(mat.min(axis=1).tolist()),(mat.flatten().min())]
        sum=[(mat.sum(axis=0).tolist()),(mat.sum(axis=1).tolist()),(mat.flatten().sum())]

        calculations={
            "mean":mean,

            "variance":var,

            "std":std,

            "maximum":max,

            "minimum":min,

            "sum":sum,

}
        return calculations