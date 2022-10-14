import main
import pytest

def test_write():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6] 
    merged_list = []
    result = [1, 2, 3, 4, 5, 6]
    main.mergeList(list1, list2, merged_list) 
    assert merged_list == result

def test_parse():
    main.FindingDates('Backend/input.csv', 'Backend/test.csv')
    assert True