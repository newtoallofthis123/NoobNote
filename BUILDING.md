# NoobNote Compiling and Building Guide

NoobNote and it's sisters as I am calling them are pretty easy to compile. You can easily compile them with any of the popular compilers for python out there like [pyinstaller](https://www.pyinstaller.org/), [winpython](https://winpython.github.io/), [nuitka](https://nuitka.net/). I recommend you use pyinstaller if you are a beginner just because it is so easy to use. I personally use nuitka and the prebuilt binaries of NoobNote provided in the [releases](https://github/newtoallofthis123/releases) pageare actually compiled with nuitka.

Below is the exact command used to compile NoobNote binaries with powershell

```powershell
python -m nuitka --standalone --windows-disable-console --windows-icon-from-ico="icon.ico" --windows-company-name="NoobScience" --windows-product-name="NoobNote" --windows-file-version=0.1  --windows-product-version=0.1 --windows-file-description="My Take on NotePad" --plugin-enable=tk-inter --python-arch="x86" NoobNote.py
```

# Build It on your own

1. First clone into the github repository of [NoobNote](https://github.com/newtoallofthis123/NoobNote)

```shell
git clone https://github.com/newtoallofthis123/NoobNote.git
```

2. Next Change into the directory

```bash
cd NoobNote
```

3. Run the command below to compile any NoobNote branch

```bash
python -m nuitka --standalone --windows-disable-console --windows-icon-from-ico="icon.ico" --windows-company-name="NoobScience" --windows-product-name="NoobNote" --windows-file-version=0.1  --windows-product-version=0.1 --windows-file-description="My Take on NotePad" --plugin-enable=tk-inter --python-arch="x86" NoobNote.py
```

4. Once the compilation is over, transfer the following assets from main directory to NoobNote.dist.
- icon.ico

- README.txt

- hotkeys.txt

- setting.ini

- LICENSE

- database.db

- README.md
5. Once You do that, run NoobNote.exe and There you have it. Hope you enjoy using it

# Pyinstaller
pyinstaller is for beginners. Try this in the terminal, bash/git bash/cmd/powershell
```shell
pyinstaller -w - i "icon.ico" -n "NoobNote"
```

# Pypi

If you are feeling courageous and know a little python, try to modify and upload NoobNote to [pypi](https://pypi.org). NoobNote already has a pypi version that you can call from the command line with 

```shell
NoobNote
```

 If you do upload it to pypi, be sure to send me a email at [noobscience](mailto:noobscience123@gmail.com), so I can link it and well test it and use it myself. 

## Thanks For Finding NoobNote Interesting

> NoobScience


