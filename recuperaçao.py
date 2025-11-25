
print( notas_recuperacao ) = [7.5, 8.0,  6.0, 9.0, 5.5]
print("Notas de recuperação:", notas_recuperacao)

print( media_recuperacao) = sum(notas_recuperacao) / len(notas_recuperacao)
print("media de recuperação:",media_recuperacao)

print(aprovados_recuperacao) = [nota for nota in notas_recuperacao if nota >= 7.0]
print("Alunos aprovados na recuperação:", aprovados_recuperacao)

nota_maxima_recuperacao = max(notas_recuperacao)
