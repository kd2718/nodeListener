# -*- mode: python -*-
a = Analysis(['quick_plots.py'],
             pathex=['C:\\Users\\Kodon\\src\\nodeapp\\listenerWS\\plots'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='quick_plots.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
