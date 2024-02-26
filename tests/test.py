from mypackage import myModule


def test_top_n():
    """"
    ake sure top_n works correctly
    """
    assert myModule.top_n([8,0,1,-1,3],3)==[8,3,1] , 'Incorrect'
    assert myModule.top_n([18,0,1,-1,13],2)==[18,13] , 'Incorrect'
    assert myModule.top_n([8,10,11,-1,1],1)==[11] , 'Incorrect'