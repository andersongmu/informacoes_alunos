import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Nota1': [8.5, 7.2, 6.8, 9.0],
    'Nota2': [7.9, 6.5, 8.2, 9.5],
    'Nota3': [9.2, 8.8, 7.5, 8.9]
}

df = pd.DataFrame(data)

df['Média'] = df[['Nota1', 'Nota2', 'Nota3']].mean(axis=1)

aluno_maior_media = df.loc[df['Média'].idxmax()]

plt.bar(df['Nome'], df['Média'])
plt.xlabel('Aluno')
plt.ylabel('Média')
plt.title('Média das notas dos alunos')
plt.xticks(rotation=45)

plt.annotate('Maior média: {:.2f}'.format(aluno_maior_media['Média']),
             xy=(aluno_maior_media['Nome'], aluno_maior_media['Média']),
             xytext=(0, 20),
             textcoords='offset points',
             arrowprops=dict(arrowstyle='->'))

plt.show()
