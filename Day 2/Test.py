import day2
import pytest
@pytest.mark.parametrize("to,ing,max,pal,uniq,dic",[(2,2,['tonight','nothing'],['Malayalam', 'mom', 's'],['tonight', 'nothing', 'Malayalam', 'mom', 's', 'Hi', 'everyone', 'How', 'are', 'you', "I'm", 'fine'],{1: 'tonight', 2: 'nothing', 3: 'tonight', 4: 'nothing', 5: 'Malayalam', 6: 'mom', 7: 's', 8: 'Hi', 9: 'everyone', 10: 'How', 11: 'are', 12: 'you', 13: "I'm", 14: 'fine'})])
def test_method(to,ing,max,pal,uniq,dic):
    assert to==day2.TO
    assert ing==day2.ING
    assert max==day2.maxList
    assert pal==day2.palindrome
    assert uniq==day2.uniqueList
    assert dic==day2.Word