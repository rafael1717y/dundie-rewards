import os
import uuid
import pytest 
from dundie.core import load
from .constants import PEOPLE_FILE


# hooks tradicionais
def setup_module():
    print('Roda antes dos testes desse módulo.\n')
    print()


def teardown_module():
    print()
    print("Roda apos os testes desse módulo.\n")



@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso é sujeira...")
    yield
    file_.remove()



@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Teste load function"""
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt" # apaga o arquivo ao final tmp
    request.addfinalizer(lambda: os.unlink(filepath)) 
    
    with open(filepath, "w") as file_: #teste cria o arquivo
        file_.write("dados uteis somente paa o teste.")
    
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Teste load function"""
    
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados uteis somente paa o teste.")
    
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'
