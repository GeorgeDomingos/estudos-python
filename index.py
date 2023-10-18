notas = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 88,
    "Eve": 64
}

maior_nota = 0
nome = ""

for aluno,nota in notas.items():
  if nota> maior_nota:
    maior_nota=nota
    nome=aluno

print(nome)