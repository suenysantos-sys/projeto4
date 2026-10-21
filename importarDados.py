import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.sqlite3"
CSV_PATH = BASE_DIR / "base_filmes.csv"


def importar_dados():
    conn = sqlite3.connect(DB_PATH)

    try:
        with conn:
            with CSV_PATH.open(
                newline="",
                encoding="utf-8-sig"
            ) as csvfile:

                leitor = csv.DictReader(csvfile)

                for linha in leitor:
                    nome_genero = linha["genero"].strip()
                    titulo = linha["titulo"].strip()
                    descricao = linha["descricao"].strip()
                    ano = int(
                        linha.get("ano_lancamento", linha.get("ano", "0"))
                    )
                    duracao = int(linha["duracao"])

                    # Busca ou cadastra o gênero
                    resultado = conn.execute(
                        """
                        SELECT id
                        FROM filmes_generos
                        WHERE nome = ?
                        """,
                        (nome_genero,),
                    ).fetchone()

                    if resultado:
                        genero_id = resultado[0]
                    else:
                        cursor = conn.execute(
                            """
                            INSERT INTO filmes_generos (nome)
                            VALUES (?)
                            """,
                            (nome_genero,),
                        )
                        genero_id = cursor.lastrowid

                    # Evita importar o mesmo filme duas vezes
                    filme_existente = conn.execute(
                        """
                        SELECT id
                        FROM filmes_filmes
                        WHERE titulo = ?
                        """,
                        (titulo,),
                    ).fetchone()

                    if filme_existente:
                        print(f"Filme já cadastrado: {titulo}")
                        continue

                    # Insere o filme
                    conn.execute(
                        """
                        INSERT INTO filmes_filmes
                            (titulo, descricao, ano_lancamento,
                             genero_id, duracao)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (
                            titulo,
                            descricao,
                            ano,
                            genero_id,
                            duracao,
                        ),
                    )

                    print(f"Filme importado: {titulo}")

    finally:
        conn.close()

    print("Importação de filmes concluída!")


if __name__ == "__main__":
    importar_dados()