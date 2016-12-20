Add-Type -AssemblyName System.Windows.Forms
[Reflection.Assembly]::LoadWithPartialName("System.Drawing")
function screenshot([Drawing.Rectangle]$bounds, $path) {
   $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height
   $graphics = [Drawing.Graphics]::FromImage($bmp)

   $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size)

   $bmp.Save($path)

   $graphics.Dispose()
   $bmp.Dispose()
}

While($True){

    $width = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width
    $height = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height
    $bounds = [Drawing.Rectangle]::FromLTRB(0, 0, $width, $height)

    $timestamp = get-date -Format ddMMyhhmmss
    $filename = "C:\bin\screenshot" + $timestamp + ".jpg"

    screenshot $bounds $filename
    
    Start-Sleep 900
}