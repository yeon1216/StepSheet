def get_row_value_from_date(date_str):
    day_str = date_str.split(' ')[1]
    n = int(day_str[:-1])
    return get_value(n)


def get_value(num):
    date_row_str = "E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AF,AG,AH,AI"
    date_row = date_row_str.split(',')
    return date_row[num-1]


if __name__ == '__main__':
    print(get_value(1))
    print(get_value(2))
    print(get_value(3))
    print(get_value(22))
    print(get_value(23))
    print(get_value(30))