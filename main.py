entrada = input('Informe a sequencia de DNA: ').upper()

def dna(entrada):
  vogais = 'AEIOU'
  consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'
  resultado = ''
  for i in range(len(entrada)):
    if entrada[i] in 'ACTG':
        resultado += entrada[i]
  
        if i < len(entrada) - 1:
          if (entrada[i] in vogais and entrada[i+1] in consoantes) or (entrada[i] in consoantes and entrada[i+1] in vogais):
           resultado += ' '
  return resultado
  print(resultado)

print(dna(entrada))