"""Publication audits distinguish archives from incidental ZIP-like file bytes."""
import importlib.util
from pathlib import Path
import struct
import sys
import zipfile
import pytest

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('method_audit',ROOT/'scripts/check-method-package.py')
audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)


def test_ordinary_output_with_zip_signature_is_scanned_as_content(tmp_path,monkeypatch):
    # A ZIP end marker can occur in browser assets without a valid central directory.
    (tmp_path/'asset.js').write_bytes(b'normal browser asset'+struct.pack('<4s4H2LH',b'PK\x05\x06',0,0,1,1,100,999,0))
    monkeypatch.setattr(sys,'argv',['audit','--published',str(tmp_path)])
    audit.main()


def test_archive_members_are_checked_for_private_tooling_references(tmp_path,monkeypatch):
    with zipfile.ZipFile(tmp_path/'download.zip','w') as archive:
        archive.writestr('README.txt','private tooling: '+'-'+'agents')
    monkeypatch.setattr(sys,'argv',['audit','--published',str(tmp_path)])
    with pytest.raises(ValueError,match='Private tooling reference'):
        audit.main()
