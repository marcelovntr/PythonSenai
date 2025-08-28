"""
Exemplo básico de uso do pandas

Este código demonstra as operações mais básicas com pandas:
1. Criação de um DataFrame simples
2. Visualização dos dados
3. Operações básicas com colunas

Como usar:
1. Execute o programa
2. Observe os diferentes outputs no console
"""

import pandas as pd #pd é apenas um alias

def main():
    # Criando um DataFrame simples com notas de alunos
    dados = {
        'Aluno': ['João', 'Maria', 'Pedro', 'Ana', 'Bossa', 'Joselito'],
        'Nota': [8.5, 6.9, 4.5, 8.0, 10.0, 6.5]
    }
    
    # Criando o DataFrame
    df = pd.DataFrame(dados)
    
    print("\nDataFrame com notas dos alunos:")
    print(df)
    
    # Calculando a média das notas
    media = df['Nota'].mean()
            #df.Nota.mean()
    print(f"\nMédia das notas: {media:.2f}")
    
    # Mostrando a maior nota
    maior_nota = df['Nota'].max()
    print(f"Maior nota: {maior_nota}")
    
    # Mostrando a menor nota
    menor_nota = df['Nota'].min()
    print(f"Menor nota: {menor_nota}")

    #********************************** WINDSURF ****************************************
    print("\nAlunos com nota maior ou igual a 8:")
    print(df[df['Nota'] >= 8])
    print("\n DF Final: ")
   

    df['Aprovado'] = df['Nota'] >= 7
    # print("\nDataFrame com coluna 'Aprovado':")
    # print(df)

    #não permite df.Recuperacao = ...
    df['Recuperacao'] = (df.Nota < 7) & (df.Nota >= 5)
    df['Reprovado'] = df.Nota < 5
    print(df) 

    # ✅ 3. Ordenar os alunos pela nota (decrescente)
    #     print("\nAlunos ordenados por nota (maior para menor):")
    #     print(df.sort_values(by='Nota', ascending=False))
    # ✅ 4. Ver estatísticas básicas com describe()
    #     print("\nEstatísticas descritivas:")
    #     print(df['Nota'].describe())
    # ✅ 5. Renomear colunas
    #     df.rename(columns={'Aluno': 'Nome do Aluno', 'Nota': 'Nota Final'}, inplace=True)
    #     print("\nDataFrame com colunas renomeadas:")
    #     print(df)
    # ✅ 6. Salvar em CSV
    #     df.to_csv('notas_alunos.csv', index=False)
    # ✅ 7. Ler de um CSV (caso queira carregar depois)
    #     df_novo = pd.read_csv('notas_alunos.csv')
    #     print("\nDataFrame carregado do CSV:")
    #     print(df_novo)
    # ✅ 8. Salvar em Excel
    #     df.to_excel('notas_alunos.xlsx', index=False)
    # ✅ 9. Ler de um Excel (caso queira carregar depois)
    #     df_novo = pd.read_excel('notas_alunos.xlsx')
    #     print("\nDataFrame carregado do Excel:")
    #     print(df_novo)

if __name__ == "__main__":
    main() 