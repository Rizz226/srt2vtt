import setuptools

long_description = open("README.md").read()
required = ['webvtt-py'] # Comma seperated dependent libraries name

setuptools.setup(
    name="srt2vtt",
    version="1.0",
    author="Chase Anderson",
    author_email="Chase@Anderson.vet",
    license="",
    description="A simple wrapper for webvtt-py to allow users to quickly convert SRT to VTT files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rizz226/srt2vtt",
    key_words="<KEY WORDS>",
    install_requires=['webvtt-py'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
        'srt2vtt=srt2vtt.py:main']
    }
)