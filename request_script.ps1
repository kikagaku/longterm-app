# PowerShell スクリプト
$url = "https://longterm-firstapi.onrender.com/make_predictions"

$headers = @{
    'accept' = 'application/json'
    'Content-Type' = 'application/json'
}

$body = @{
    sepal_length = 5.9
    sepal_width = 3.0
    petal_length = 5.1
    petal_width = 1.8
} | ConvertTo-Json  # ハッシュテーブルをJSONに変換

$response = Invoke-RestMethod -Method Post -Uri $url -Headers $headers -Body $body

# 応答の内容を表示する
$response | ConvertTo-Json -Depth 32 | Write-Output
