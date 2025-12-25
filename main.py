from src.pipeline import Pipeline


pipeline = Pipeline()


validos, rejeitados, relatorio = pipeline.run("data/raw/clientes.csv")


validos.to_csv("data/processed/validos.csv", index=False)
rejeitados.to_csv("data/processed/rejeitados.csv", index=False)


with open("data/reports/validation_report.txt", "w") as f:
    for k, v in relatorio.items():
        f.write(f"{k}: {v}\n")


print("Processamento finalizado 🚀")