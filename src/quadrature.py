def trapezoid(f, lower, upper, N):
    h = (upper - lower) / N
    area = 0
    for i in range(N+1):
        x = lower + i * h
        if (i == 0) or (i == N):
            area += f(x)/2
        else:
            area += f(x)
    area = area * h
    return area