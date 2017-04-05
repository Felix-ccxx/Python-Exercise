def sparse_vector (indices, values):
    vector = [indices, values]
    ind = values.index(max(values))
    print indices[ind], values[ind]
    return vector
    
indices=[1, 8, 231, 500]
values=[0.1, 2.3, 2.0, 10.0]

res=sparse_vector(indices, values)
