[CmdletBinding()]
param(
    [switch]$InstallDependencies
)

$ErrorActionPreference = 'Stop'
$python = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
$source = Join-Path $PSScriptRoot 'docs'

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw 'Missing .venv/Scripts/python.exe. Create the project virtual environment first.'
}

& $python -c "import sys; assert sys.version_info >= (3, 11), 'Documentation tooling requires Python 3.11 or newer.'"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

if ($InstallDependencies) {
    & $python -m pip install -r (Join-Path $PSScriptRoot 'requirements-docs.txt')
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

& $python -c 'import sphinx, sphinx_needs, sphinx_rtd_theme, myst_parser, matplotlib'
if ($LASTEXITCODE -ne 0) {
    Write-Error 'Documentation dependencies are missing or cannot be imported. Run .\build-docs.ps1 -InstallDependencies.' -ErrorAction Continue
    exit $LASTEXITCODE
}

& $python (Join-Path $PSScriptRoot 'scripts/build_docs.py') $source
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
