import pytest
import day2task as day

list1 = ['hello', 'world', 'python', 'training', 'ADF', 'day3']
method3_list= ['h', 'll', 'w', 'rld', 'PYTH', 'n', 'tr', 'n', 'ng', 'DF', 'd', 'y3']
@pytest.mark.parametrize("res,expected",[(['hello', 'world', 'python', 'training', 'ADF', 'day3'],'hello')])
def test_method1(res,expected):
    assert  day.Results.getrepeatstr(day.Results,res) == expected
def test_method2():
    res1=day.Filecls.getpalindrome(day.Results,list1)
    assert res1 == []

def test_method3():
    res=day.Filecls.unifileops(day.Results, list1)
    assert method3_list==res

def test_fileread():
    res = day.Filecls.fread(day.Results)
    assert res
    
def test_to():
    res1=day.Filecls.prefixcount(day.Results,list1)
    assert res1 == 0
def test_ing():
    res1=day.Filecls.suffixcount(day.Results,list1)
    assert res1 == 1

    
