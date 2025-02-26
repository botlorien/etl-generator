import csv
from faker import Faker
import random

def gerar_csv_com_faker(nome_arquivo="dados_ficticios.csv", total_registros=1000):
    # Define um 'locale' em português (opcional)
    fake = Faker('pt_BR')
    
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, delimiter=';')

        # Cabeçalho
        escritor.writerow(["id", "nome", "idade", "email", "salario", "data_admissao"])

        for i in range(1, total_registros + 1):
            nome = fake.name()
            idade = random.randint(18, 65)
            email = fake.email()
            # Exemplo de salário aleatório entre 1500 e 20000
            salario = round(random.uniform(1500, 20000), 2)
            # Data de admissão aleatória entre 2010 e 2023
            data_admissao = fake.date_between(start_date='-13y', end_date='today')

            escritor.writerow([
                i,
                nome,
                idade,
                email,
                salario,
                data_admissao.isoformat()
            ])

    print(f"Arquivo '{nome_arquivo}' gerado com {total_registros} registros.")

if __name__ == "__main__":
    gerar_csv_com_faker("dados_ficticios.csv", 1000)
