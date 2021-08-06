@echo off
echo NoobNote Compiler
python -m nuitka --standalone --windows-disable-console --windows-icon-from-ico="icon.ico" --windows-company-name="NoobScience" --windows-product-name="NoobNote" --windows-file-version=0.1  --windows-product-version=0.1 --windows-file-description="My Take on NotePad" --plugin-enable=tk-inter --python-arch="x86" NoobNote.py
echo Done
echo NoobScience