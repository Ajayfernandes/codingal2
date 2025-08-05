def divide(dividend, divisor):
    sign = (-1 if ((dividend<0) ^ (divisor < 0)) else 1)
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient_num = 0
    temp_num = 0
    for i in range(31,-1,-1):
        if (temp_num + (divisor << i ) <= dividend):
            temp_num += divisor << i
            quotient_num |= 1<<i
    if sign == -1:
        quotient_num = -quotient_num
    return quotient_num
    
print(divide(2, 2))
            