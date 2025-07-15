class DataScientist:
    def __init__(self):
        # Personal Info
        self.name = "Gustavo Chiappe"
        self.title = "Data Analyst | Python Developer | Economía Aplicada"
        self.location = "Buenos Aires, Argentina"
        self.contact = {
            "email": "chiappegus@gmail.com",
            "linkedin": "linkedin.com/in/gustavo-c-9a53059/",
            "github": "github.com/chiappegus",
            "kaggle": "kaggle.com/gchiappe"
        }
        
        # Core Skills
        self.skills = {
            "Lenguajes": ["Python", "R", "Java", "Solidity", "SQL"],
            "Machine Learning": ["Scikit-Learn", "TensorFlow", "PyTorch", "XGBoost", "Hugging Face"],
            "Cloud & Big Data": ["AWS", "Google Cloud", "Azure", "Spark", "Docker"],
            "Visualización": ["Pandas", "Matplotlib", "Seaborn", "Plotly"]
        }
        
        # Experience
        self.experience = [
            {
                "role": "Analista/DEV de la Información",
                "company": "Ministerio de Agroindustria - Dirección Nacional de Emergencias Agropecuarias",
                "period": "2016 - Actual",
                "achievements": [
                    "Desarrollo de formularios digitales con geolocalización (Google Maps API)",
                    "Automatización de reportes para gestión de emergencias"
                ]
            },
            {
                "role": "Analista QA",
                "company": "IBM/Telefónica (LMYA SRL)",
                "period": "2007 - 2008",
                "achievements": [
                    "Mantenimiento de interfaces para usuarios",
                    "Control de calidad y testing funcional"
                ]
            }
        ]
        
        # Education
        self.education = [
            {
                "degree": "Maestría en Economía Aplicada",
                "institution": "Universidad Católica Argentina",
                "year": "2014-2015"
            },
            {
                "degree": "Ingeniería en Producción Agropecuaria",
                "institution": "Universidad Católica Argentina",
                "year": "2005"
            }
        ]
        
        # Proyectos Kaggle (ahora como método!)
        self.kaggle_projects = [
            {
                "name": "Predicción de Cáncer de Mama",
                "url": "https://kaggle.com/code/gchiappe/breast-cancer-wisconsin-gustavo-predic-logistic",
                "tech": ["Scikit-Learn", "Pandas", "Matplotlib"],
                "description": "Modelo de regresión logística (accuracy 0.95) para clasificación de tumores"
            },
            {
                "name": "Árbol de Decisión (Titanic)",
                "url": "https://kaggle.com/code/gchiappe/decision-tree-accuracy-0-7686567164179104",
                "tech": ["Scikit-Learn", "Seaborn"],
                "description": "Accuracy 0.77 con feature engineering"
            }
        ]
    
    def __str__(self):
        return f"{self.name} | {self.title} | {self.location}"
    
    def show_projects(self):
        print("\n🚀 Proyectos Destacados en Kaggle:")
        for project in self.kaggle_projects:
            print(f"\n🔹 {project['name']}")
            print(f"   - Tecnologías: {', '.join(project['tech']}")
            print(f"   - URL: {project['url']}")
    
    def optimize_portfolio(self):
        return "Optimizando modelos financieros con Machine Learning y Python 🚀"
    
    def contact_me(self):
        print("\n📬 Contáctame:")
        for platform, url in self.contact.items():
            print(f"   - {platform.capitalize()}: {url}")

# Instancia y demo
if __name__ == "__main__":
    gustavo = DataScientist()
    
    print("="*50)
    print(gustavo)
    print("="*50)
    
    gustavo.show_projects()
    print("\n💡 Método especial:")
    print(gustavo.optimize_portfolio())
    
    gustavo.contact_me()
    print("\n" + "="*50)
