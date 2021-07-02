# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['29_pyqt5_공학용계산기.py'],
             pathex=['/Users/admin/PycharmProjects/Online_Intermediate_Course'],
             binaries=[],
             datas=[("./calculator.ui", ".")],
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
          name='29_pyqt5_공학용계산기',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='29_pyqt5_공학용계산기.app',
             icon=None,
             bundle_identifier=None)
