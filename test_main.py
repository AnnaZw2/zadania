def test1_suma():
    #given
    lista=[1,2,2,10]
    #when
    result=suma(lista)
    #then
    assert result==15

def test2_suma():
    #given
    lista=[]
    #when
    result=suma(lista)
    #then
    assert result==0

def test1_kwadrat(capsys):
    #given
    liczba=3
    #when
    kwadrat(liczba)
    result=capsys.readouterr()
    #then
    assert result.out=='9\n'
    assert result.err == ''

def test2_kwadrat(capsys):
    #given
    liczba=0
    #when
    kwadrat(liczba)
    result=capsys.readouterr()
    #then
    assert result.out=='0\n'
    assert result.err==''
