Add-Type -AssemblyName System.Drawing
$dir = "c:\Users\Dell\OneDrive\Desktop\ISHAN SRIVASTAV\practice"

Get-ChildItem -Path $dir -Filter *.jpg | Where-Object { $_.Length -gt 5MB } | ForEach-Object {
    $filePath = $_.FullName
    Write-Host "Processing $filePath"
    
    try {
        $img = [System.Drawing.Image]::FromFile($filePath)
        
        # Calculate new dimensions (max width/height 1920)
        $ratio = 1
        if ($img.Width -gt 1920 -or $img.Height -gt 1920) {
            $ratio = [math]::Min(1920.0 / $img.Width, 1920.0 / $img.Height)
        } else {
            # Let's scale down by 50% if it's already under 1920 but somehow over 5MB
            $ratio = 0.5
        }
        
        $newWidth = [math]::Max([int]($img.Width * $ratio), 1)
        $newHeight = [math]::Max([int]($img.Height * $ratio), 1)
        
        $newImg = New-Object System.Drawing.Bitmap $newWidth, $newHeight
        $graph = [System.Drawing.Graphics]::FromImage($newImg)
        $graph.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graph.DrawImage($img, 0, 0, $newWidth, $newHeight)
        
        $img.Dispose()
        
        # Save as JPEG with good compression
        $eps = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $ep = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]75)
        $eps.Param[0] = $ep
        
        $codecs = [System.Drawing.Imaging.ImageCodecInfo]::GetImageDecoders()
        $jpegCodec = $codecs | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid } | Select-Object -First 1
        
        $newImg.Save($filePath, $jpegCodec, $eps)
        $newImg.Dispose()
        
        Write-Host "Successfully compressed: $filePath"
    } catch {
        Write-Host "Error processing $filePath : $_"
    }
}
Write-Host "Done!"
