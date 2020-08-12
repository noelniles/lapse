# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/me/git/lapse/src/main/python/main.py'],
             pathex=['/home/me/git/lapse/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/me/venvs/lapse3.7/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/home/me/git/lapse/target/PyInstaller/fbs_pyinstaller_hook.py'],
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
          name='lapse',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='lapse')
