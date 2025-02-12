class GustavoChiappe:
    def __init__(self):
        self.name = "Gustavo Chiappe"
        self.location = "Buenos Aires, Argentina"
        self.email = "chiappegus@gmail.com"
        self.linkedin = "linkedin.com/in/gustavo-c-9a53059/"
        self.github = "github.com/chiappegus"
        
        self.skills = [
            "Python", "R", "Machine Learning", "Quant Finance",
            "Scikit-Learn", "TensorFlow", "PyTorch", "XGBoost", "SQL",
            "AWS", "Google Cloud AI/ML", "Docker", "Spark (MLlib)"
        ]
        
        self.experience = {
            "Ministerio de Agroindustria": "Analista/DEV de la Información (2016 - Actual)",
            "IBM-Telefónica": "Analista QA (2007 - 2008)"
        }

        self.education = {
            "Maestría en Economía Aplicada": "Universidad Católica Argentina",
            "Finanzas Cuantitativas QUANT": "UCEMA (2024)",
            "AI / Data Science": "Universidad de Palermo (2024)"
        }

    def optimize_portfolio(self):
        return "Optimizing financial models with Machine Learning 🚀"

gustavo = GustavoChiappe()
print(gustavo.optimize_portfolio())
