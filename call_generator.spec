# -*- mode: python ; coding: utf-8 -*-
import os
import sys
block_cipher = None
site_package_path = r"C:\Users\YH\AppData\Local\Programs\Python\Python310\Lib\site-packages"

a = Analysis(['call_generator.py'],
             pathex=[],
             binaries=[('./template.docx','.'), ('./ico.ico','.')],
             datas=[(os.path.join(site_package_path,'docx','templates'), 'docx/templates'), (os.path.join(site_package_path, 'docxcompose', 'templates'), 'docxcompose/templates')],
             hiddenimports=['python-docx', 'docxcompose'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='TableGenerator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='ico.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='TableGenerator')
