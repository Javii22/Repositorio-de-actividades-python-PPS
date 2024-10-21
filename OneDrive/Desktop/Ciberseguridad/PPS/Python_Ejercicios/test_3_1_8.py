from P3_1_8 import*
import py_test

def esPalindromo(palabra: str):

    assert esPalindromo("radar") == True
    assert esPalindromo("ana") == True

    assert esPalindromo("python") == False
    assert esPalindromo("hola") == False

if __name__ == "__main__" :
    py_test.main()