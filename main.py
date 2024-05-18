def eh_palindromo(texto):
    texto = texto.replace("-", "").replace(" ", "").lower()
    return texto == texto[::-1]
    
    
print(eh_palindromo("socorram-me subi no onibus em marrocos"))
