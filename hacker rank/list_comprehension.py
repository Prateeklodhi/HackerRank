
def function(x, y, z, n):
    make_list = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]
    not_equal_to_list = [list_ex for list_ex in make_list  if sum(list_ex) != n]
    return not_equal_to_list


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    function(x,y,z,n)


