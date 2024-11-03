import ccxt

# OKX 선물 거래소 객체 생성
exchange = ccxt.okx({
    'options': {
        'defaultType': 'swap',  # 무기한 선물 거래를 위한 설정
    },
})

# 거래소의 시장 데이터 로드
exchange.load_markets()

# 조회할 암호화폐 심볼 리스트
symbols = ['BTC/USDT:USDT', 'ETH/USDT:USDT', 'SOL/USDT:USDT', 'BNB/USDT:USDT']

def fetch_funding_rate(symbol):
    try:
        # 펀딩 비율 정보 조회
        funding_info = exchange.fetch_funding_rate(symbol)
        funding_rate = funding_info['fundingRate']
        return funding_rate
    except Exception as e:
        print(f"{symbol}의 펀딩 비율을 가져오는 중 오류 발생: {e}")
        return None

for symbol in symbols:
    funding_rate = fetch_funding_rate(symbol)
    if funding_rate is not None:
        if funding_rate >= 0:
            print(f"{symbol}: 펀딩 비율이 양수입니다. ({funding_rate})")
        else:
            print(f"{symbol}: 펀딩 비율이 음수입니다. ({funding_rate})")
