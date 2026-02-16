from setuptools import setup,find_packages

def get_libraries(path):
    libraries=[]
    with open(path,"r") as file:
        content=file.readlines()
        content=[lib.replace("\n","") for lib in content]
        if "-e ." in content:
            content.remove("-e .")
        libraries.extend(content)
    
    return libraries
setup(

    name="Insurance_Price_prediction",
    version="0.1.0",
    description="Insurance Price Prediction Using Regression Models",
    author="Vijay Kumar Bandaru",
    author_email="Vijay Kumar",
    packages=find_packages(),
    install_requires=get_libraries("requirements.txt")


)