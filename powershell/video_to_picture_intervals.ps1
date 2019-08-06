if([string]::IsNullOrEmpty($FilePath) -Or (Test-Path -LiteralPath $FilePath -PathType Leaf) -eq $false) {
  [void][System.Reflection.Assembly]::LoadWithPartialName("System.windows.forms")    
  $dialog = New-Object System.Windows.Forms.OpenFileDialog
  $dialog.Filter = "VIDEO FILE(*.MOV;*.MP4;*.AVI)|*.MOV;*.MP4;*.AVI"
  $dialog.InitialDirectory = "~/Desktop"
  $dialog.Title = "Choose the video file"

  if($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK){
    ./python-3.6.8-embed-amd64/python ./src/video_to_picture_intervals.py $dialog.FileName
  }
}
