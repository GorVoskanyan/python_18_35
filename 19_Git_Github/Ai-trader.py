# pip install ccxt pandas ta

import ccxt
import pandas as pd
import ta

api_key = 'your_api_key'
api_secret = 'your_api_secret'
symbol = 'BTC/USDT'
timeframe = '1h'
limit = 100

exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

def fetch_data(symbol, timeframe, limit):
    bars = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

def calculate_indicators(df):
    df['SMA_20'] = ta.trend.sma_indicator(df['close'], window=20)
    df['SMA_50'] = ta.trend.sma_indicator(df['close'], window=50)
    return df

def generate_signal(df):
    if df['SMA_20'].iloc[-1] > df['SMA_50'].iloc[-1] and df['SMA_20'].iloc[-2] <= df['SMA_50'].iloc[-2]:
        return 'BUY'
    elif df['SMA_20'].iloc[-1] < df['SMA_50'].iloc[-1] and df['SMA_20'].iloc[-2] >= df['SMA_50'].iloc[-2]:
        return 'SELL'
    return 'HOLD'

def place_order(signal, symbol, amount):
    if signal == 'BUY':
        print(f'Placing buy order for {amount} of {symbol}')
        # exchange.create_market_buy_order(symbol, amount)
    elif signal == 'SELL':
        print(f'Placing sell order for {amount} of {symbol}')
        

def main():
    df = fetch_data(symbol, timeframe, limit)
    df = calculate_indicators(df)
    signal = generate_signal(df)
    print(f'Signal: {signal}')
    
    amount = 0.01
    place_order(signal, symbol, amount)

if __name__ == "__main__":
    main()