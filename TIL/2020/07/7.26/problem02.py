def my_number(n, m):
    nums = (f'010-{n}-{m}')
    return nums


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(my_number(1234, 5678))
    # => '010-1234-5678'
    print(my_number(1000, 9999))
    # => '010-1000-9999'