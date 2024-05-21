# Check if Python is installed
$python = Get-Command python -ErrorAction SilentlyContinue

if (-not $python) {
    Write-Host "Python is not installed. Please install Python first."
    exit 1
}

# Check if pip is installed
$pip = Get-Command pip -ErrorAction SilentlyContinue

if (-not $pip) {
    Write-Host "pip is not installed. Installing pip..."
    python -m ensurepip --upgrade
    $pip = Get-Command pip -ErrorAction SilentlyContinue
    if (-not $pip) {
        Write-Host "pip installation failed. Please install pip manually."
        exit 1
    }
}

# Install the groq package using pip
Write-Host "Installing the 'groq' package..."
pip install groq

# Verify installation
if ($?) {
    Write-Host "'groq' has been successfully installed."
} else {
    Write-Host "Failed to install 'groq'."
}
