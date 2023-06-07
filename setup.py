import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="colors",
    version="4.0.4",
    author="Idris Vohra",
    author_email="idrishaider987@gmail.com",
    packages=["colors"],
    description="Colors, text formats, decorations and much more for TERMINAL",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
