'''
1.pytest
  =>pip install pytest [cmd]
  =>pip install pytest-html [cmd]
'''
import pytest
def test_addition():
     num1=2
     num2=3
     assert num1+num2==5  # expected = actual?

def test_multiply():
     num1=2
     num2=3
     assert num1*num2==6  # expected = actual?

'''
  1.blur
  2.user name
  3.password
  4. user,pass (wrong)
  5. user(wrong),password
  6. user(wrong),password(wrong)
  7.pass
'''


@pytest.mark.parametrize("a,b,expected",[
     (1,2,3),
     (2,3,5),
     (10,20,30)
])
def test_para_add(a,b,expected):
     assert a+b==expected



@pytest.fixture
def sample_data():
     return {"name":"maung maung","age":20} # dict


def test_data(sample_data):

     assert sample_data["age"]==20
     assert sample_data["name"]=="maung maung"
     


@pytest.mark.skip(reason="No need to run")
def test_skip():
     assert 2+3==4


@pytest.mark.parametrize("input_dict,expected",[
     ({"a":1,"b":2},3),
     ({"x":10,"y":20},30),
     ({"num1":10,"num2":21},31)
])
def test_dict_addition(input_dict,expected):
     # print(input_dict.values())
     # print(input_dict.keys())
     # print(input_dict.items())
     # for key in input_dict.keys():
     #      print(key)
     for key,value in input_dict.items():
          print(key,value)
     assert sum(input_dict.values())==expected


@pytest.fixture
def fixure_a():
     return "Fixure A"

@pytest.fixture
def fixure_b():
     return "Fixure B"

def test_multiple_fixure(fixure_a,fixure_b):
     assert fixure_a=="Fixure A"


@pytest.fixture
def setup_data():
     return {"x":10,"y":20}

@pytest.mark.parametrize("a,b,expected",[
     (1,4,15),
     (3,4,17)
])
def test_with_fixure(setup_data,a,b,expected):
     assert a+b+setup_data["x"]==expected



def find_rect_area(x,y):
     return  x*y

def test_rect_area():
     assert find_rect_area(2,3)==6
     assert find_rect_area(3,3)==9
