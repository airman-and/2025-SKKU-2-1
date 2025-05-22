# 불필요한 파일 일괄 정리 스크립트
# Github에 올리기 전에 불필요한 파일을 정리합니다

# 작업 경로 설정
$workspacePath = "C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기"

# 삭제할 파일 유형들
$fileTypesToDelete = @(
    "*.pyc",
    "*.pyo",
    "*.pyd",
    "*.so",
    "*.log",
    "*.tmp",
    "*.bak",
    "*.swp",
    "*.swo",
    "*.zip",
    "*.gz",
    "*.tar",
    "*.rar",
    "*.7z",
    "*.exe",
    "*.dll",
    "*.obj",
    "*.o",
    "*.a",
    "*.lib",
    "*.pkg",
    "*.sqlite"
)

# 삭제할 디렉토리들
$dirsToDelete = @(
    "__pycache__",
    ".ipynb_checkpoints",
    ".pytest_cache",
    ".vscode",
    "dist",
    "build",
    "*.egg-info",
    "학습로그",
    "임시파일"
)

# 삭제 진행 상황 함수
function Write-Progress-Message {
    param(
        [string]$Message
    )
    Write-Host $Message -ForegroundColor Green
}

# 1. 캐시, 빌드 파일 등의 디렉토리 삭제
Write-Progress-Message "1. 불필요한 디렉토리 삭제 중..."
foreach ($dir in $dirsToDelete) {
    $items = Get-ChildItem -Path $workspacePath -Recurse -Directory -Filter $dir -ErrorAction SilentlyContinue
    if ($items) {
        Write-Host "  - '$dir' 디렉토리 ${($items.Count)}개 삭제 중..." -ForegroundColor Yellow
        $items | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    }
}

# 2. 임시 파일, 로그 파일 등 삭제
Write-Progress-Message "2. 불필요한 파일 삭제 중..."
foreach ($fileType in $fileTypesToDelete) {
    $items = Get-ChildItem -Path $workspacePath -Recurse -File -Include $fileType -ErrorAction SilentlyContinue
    if ($items) {
        Write-Host "  - '$fileType' 파일 ${($items.Count)}개 삭제 중..." -ForegroundColor Yellow
        $items | Remove-Item -Force -ErrorAction SilentlyContinue
    }
}

# 3. 특정 불필요한 폴더 삭제 (로그 폴더, 임시파일 폴더)
$specificDirsToDelete = @(
    "$workspacePath\학습로그",
    "$workspacePath\임시파일"
)

foreach ($dir in $specificDirsToDelete) {
    if (Test-Path $dir) {
        Write-Host "  - '$(Split-Path -Leaf $dir)' 폴더 삭제 중..." -ForegroundColor Yellow
        Remove-Item -Recurse -Force $dir -ErrorAction SilentlyContinue
    }
}

# 4. 대용량 데이터 파일 정리 (10MB 이상)
Write-Progress-Message "3. 대용량 데이터 파일 검색 중..."
$largeFiles = Get-ChildItem -Recurse -Path $workspacePath -File | Where-Object { $_.Length -gt 10MB }
if ($largeFiles) {
    Write-Host "다음 대용량 파일들이 발견되었습니다. (10MB 이상):" -ForegroundColor Yellow
    foreach ($file in $largeFiles) {
        $sizeInMB = [Math]::Round($file.Length / 1MB, 2)
        Write-Host "  - $($file.FullName) ($sizeInMB MB)" -ForegroundColor Yellow
    }
    $confirmDelete = Read-Host "이 파일들을 삭제하시겠습니까? (Y/N)"
    if ($confirmDelete -eq "Y" -or $confirmDelete -eq "y") {
        $largeFiles | Remove-Item -Force
        Write-Host "대용량 파일들이 삭제되었습니다." -ForegroundColor Green
    }
}

Write-Progress-Message "정리가 완료되었습니다!"
