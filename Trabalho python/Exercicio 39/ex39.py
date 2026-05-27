import re
import csv

padrao_email = r"\S+@\S+\.\S+"

padrao_telefone = r"\d{4,5}-\d{4}"

with open("Exercicio 39/cadastro.txt", "r") as arquivo:

    with open(
        "Exercicio 39/clientes_limpos.csv",
        "w",
        newline=""
    ) as arquivo_limpo:

        writer = csv.writer(arquivo_limpo)

        writer.writerow([
            "Nome",
            "Email",
            "Telefone"
        ])

        for linha in arquivo:

            try:

                email = re.search(
                    padrao_email,
                    linha
                )

                telefone = re.search(
                    padrao_telefone,
                    linha
                )

                if not email or not telefone:

                    raise ValueError

                nome = linha

                nome = nome.replace(
                    email.group(),
                    ""
                )

                nome = nome.replace(
                    telefone.group(),
                    ""
                )

                nome = nome.strip()

                writer.writerow([
                    nome,
                    email.group(),
                    telefone.group()
                ])

            except Exception:

                print(
                    f"Linha inválida: {linha}"
                )

print("Arquivo CSV criado com sucesso!")