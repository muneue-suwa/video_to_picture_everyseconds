Param(
  [Parameter()]
  [String] $FilePath
)

if([string]::IsNullOrEmpty($FilePath) -Or (Test-Path -LiteralPath $FilePath -PathType Leaf) -eq $false) {
    [void][System.Reflection.Assembly]::LoadWithPartialName("System.windows.forms")    
    $dialog = New-Object System.Windows.Forms.OpenFileDialog
    $dialog.Filter = "VIDEO FILE|*.MOV, *.MP4, *.AVI"
    $dialog.InitialDirectory = "C:\"
    $dialog.Title = "Choose the video file"

    if($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::NG){
        exit 1
    }

    $FilePath = $dialog.FileName
}

./python-3.6.8-embed-amd64/python ../src/video_to_picture_intervals.py $FilePath