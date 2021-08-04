# [선택 과제 1] Gradient Descent

## 1. gradient_decent (1)
```python
def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    diff, _ = func_gradient(fun, val)
    while np.abs(diff) > epsilon:
        val -= lr_rate * diff
        diff, _ = func_gradient(fun, val)
        cnt += 1
    print("함수: {}\n연산횟수: {}\n최소점: ({}, {})".format(fun(val)[1], cnt, val, fun(val)[0]))
```

- sympy 라이브러리를 이용해 미분값을 구하고 value 값을 업데이트 하는 방법에 대해 이해하게 됨

## 2. gradient_decent (2)
```python
def gradient_descent(func, init_point, lr_rate=1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    ## Todo
    diff = difference_quotient(func, val)
    while np.abs(diff) > epsilon:
        val -= lr_rate * diff
        diff = difference_quotient(func, val)
        cnt += 1
    print("연산횟수: {}\n최소점: ({}, {})".format(cnt, val, func(val)))
```

- 미분 공식을 이용해 미분값을 구하고 value 값을 업데이트 1번 문제와 굉장히 유사함

## 3. Linear Regression

### 3.1 Basic function
```python
    ## Todo
    # 예측값 y
    _y = train_x * w + b

    # gradient
    gradient_w = 2 * ((_y - train_y) * train_x).mean()
    gradient_b = 2 * (_y - train_y).mean()

    # w, b update with gradient and learning rate
    w = w - lr_rate * gradient_w
    b = b - lr_rate * gradient_b

    # L2 norm과 np_sum 함수 활용해서 error 정의
    error = np.sum((train_y - _y) ** 2) / n_data
    # Error graph 출력하기 위한 부분
    errors.append(error)
```

- w 와 b의 gradient 값을 구할 때 error의 편미분 값을 이용해서 구하는 점에 대해 알게 됨

### 3.2 More complicated function
```python
    ## Todo
    error = train_y - expand_x @ beta_gd
    grad = - np.transpose(expand_x) @ error
    beta_gd = beta_gd - 0.01 * grad
```

- 다변수 함수의 목적식을 최소화 하는 beta의 그레디언트 값을 구하기 위해서 사용하는 공식의 대해 다시 확인

## 4. Stochastic Gradient Descent
```python
    ## Todo
    batch_x = np.random.choice(train_x, n_data)
    batch_y = np.zeros_like(batch_x)
    for i in range(n_data):
        batch_y[i] = func(batch_x[i])
    _y = batch_x * w + b

    # gradient
    gradient_w = 2 * ((_y - batch_y) * batch_x).mean()
    gradient_b = 2 * (_y - batch_y).mean()

    # w, b update with gradient and learning rate
    w = w - lr_rate * gradient_w
    b = b - lr_rate * gradient_b

    # L2 norm과 np_sum 함수 활용해서 error 정의
    error = np.sum((batch_y - _y) ** 2) / n_data

    # Error graph 출력하기 위한 부분
    errors.append(error)
```

- SGD는 전체 데이터를 사용하지 않고 미니배치(일부 데이터)만 사용해서 함
- 확률적으로 데이터를 선택하므로 np.random.choice() 함수 사용법 이해

문제는 해결 된 것같아 다행이고 다변수 함수의 경우 수식이 머리에 잘 들어오지 않아서 자꾸 까먹을 것 같은 기분이 들어서 잘 이해해서 내껄로 만들어야겠다고 생각함.