# Admin API
# 例如:以下代表這則廣告目的是給 20~30 歲在台灣或日本且是使用 Android 或 iOS,不限制性別
curl -X POST -H "Content-Type: application/json" \
"http://<host>/api/v1/ad" \
--data '{
"title": "AD 55",
"startAt": "2023-12-10T03:00:00.000Z",
"endAt": "2023-12-31T16:00:00.000Z",
"conditions": [
{
"ageStart": 20,
"ageEnd": 30,
"country: ["TW", "JP"],
"platform": ["android", "ios"]
}
]
}'
# Public API
# 為了簡化情境,使用者資料請直接帶在 query parameter 上
curl -X GET -H "Content-Type: application/json" \
"http://<host>/api/v1/ad?offset=10&limit=3&age=24&gender=F&country=TW&platform=ios"
# Response
# 列出符合條件的活躍廣告, limit 限制列出 3 筆
{
"items": [
{
"title": "AD 1",
"endAt": "2023-12-22T01:00:00.000Z"
},
{
"title": "AD 31",
"endAt": "2023-12-30T12:00:00.000Z"
},
{
"title": "AD 10",
"endAt": "2023-12-31T16:00:00.000Z"
}

]
}
