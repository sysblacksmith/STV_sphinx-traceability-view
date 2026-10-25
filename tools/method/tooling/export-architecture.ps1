[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$ProjectRoot,
    [string]$DiagramDirectory = 'docs/architecture/diagrams',
    [string]$Drawio = 'C:/Program Files/draw.io/draw.io.exe',
    [string]$Python = ''
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $ProjectRoot).Path
$diagrams = Join-Path $root $DiagramDirectory
if (-not $Python) { $Python = Join-Path $root '.venv/Scripts/python.exe' }
$sources = @(Get-ChildItem -LiteralPath $diagrams -Filter '*.drawio' -File)
if (-not $sources.Count) { throw "No Draw.io sources in $diagrams" }
foreach ($source in $sources) {
    $output = [System.IO.Path]::ChangeExtension($source.FullName, '.svg')
    $arguments = @('--export', '--format', 'svg', '--embed-diagram', '--output',
        ('"' + $output + '"'), ('"' + $source.FullName + '"'))
    $process = Start-Process -FilePath $Drawio -ArgumentList $arguments -WindowStyle Hidden -Wait -PassThru
    if ($process.ExitCode -ne 0) { throw "Draw.io export failed: $($source.Name)" }
}
& $Python (Join-Path $PSScriptRoot 'normalize-diagram-links.py') --diagram-dir $diagrams
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }


