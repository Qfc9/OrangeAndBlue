# -*- mode: python -*-

block_cipher = None


a = Analysis(['worker.py'],
             pathex=['C:\\Users\\elija_000\\Desktop\\Active Projects\\OrangeAndBlue\\dask'],
             binaries=[],
             datas=[('C:\\Users\\elija_000\\AppData\\Local\\Programs\\Python\\Python36/Lib/site-packages/dask/dask.yaml', './dask'), ('C:\\Users\\elija_000\\AppData\\Local\\Programs\\Python\\Python36/Lib/site-packages/distributed/distributed.yaml', './distributed')],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='worker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
