[CmdletBinding()]
param(
    [switch]$InstallDependencies
)

$ErrorActionPreference = 'Stop'
$python = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
$source = Join-Path $PSScriptRoot 'docs'
$output = Join-Path $source '_build/html'

if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw 'Missing .venv/Scripts/python.exe. Create the project virtual environment first.'
}

if ($InstallDependencies) {
    & $python -m pip install -r (Join-Path $PSScriptRoot 'requirements-docs.txt')
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

& $python -c 'import sphinx, sphinx_needs, sphinx_rtd_theme, myst_parser, matplotlib'
if ($LASTEXITCODE -ne 0) {
    Write-Error 'Documentation dependencies are missing or cannot be imported. Run .\build-docs.ps1 -InstallDependencies.' -ErrorAction Continue
    exit $LASTEXITCODE
}

& $python -m sphinx -E -a -W --keep-going -b html $source $output
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Documentation built: $(Join-Path $output 'index.html')"
