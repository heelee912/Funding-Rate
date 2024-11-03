import ccxt

# 바이낸스 선물 거래소 객체 생성
exchange = ccxt.binance({
    'options': {
        'defaultType': 'future',  # 선물 거래를 위한 설정
    },
})

# 거래소의 시장 데이터 로드
exchange.load_markets()

# 조회할 암호화폐 심볼 리스트
symbols = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT']

def fetch_funding_rate(symbol):
    try:
        # 바이낸스 선물 API 엔드포인트를 직접 호출
        url = f"https://fapi.binance.com/fapi/v1/premiumIndex?symbol={symbol}"
        response = exchange.fetch(url)
        funding_rate = float(response['lastFundingRate'])
        return funding_rate
    except Exception as e:
        print(f"{symbol}의 펀딩비율을 가져오는 중 오류 발생: {e}")
        return None

for symbol in symbols:
    funding_rate = fetch_funding_rate(symbol)
    if funding_rate is not None:
        if funding_rate >= 0:
            print(f"{symbol}: 펀딩비율이 양수입니다. ({funding_rate})")
        else:
            print(f"{symbol}: 펀딩비율이 음수입니다. ({funding_rate})")
