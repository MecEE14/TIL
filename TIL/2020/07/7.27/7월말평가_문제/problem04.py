def dec_to_bin(n):
    if n == 0:
        return ''
    else:
        return dec_to_bin(n//2) + str(n%2)

    


            

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'
