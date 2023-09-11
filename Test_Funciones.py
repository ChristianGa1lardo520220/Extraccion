from Funciones import duplicado


def test_duplicados():
    assert duplicados([1,2,3,1]) == True
    assert duplicados([1,2,3]) == False


#TODO se hace al rato
@pytest.mark.parametrize("nums, res",[([1,2,3,1],True),
                                      ([1,2,3],False),
                                      ([1,2,3,4,5], True)])

def test_duplicados_parametrizado(nums , res):
    assert duplicados(nums) == res