from binance.client import Client
from binance.exceptions import BinanceAPIException
from datetime import datetime
import time;

class User_Binance:

    def __init__(self, api_key, api_secret, last_updatedTime = '1498867200000', last_transactions = []):
        # 1 - Authentification
        self.api_key = api_key
        self.api_secret = api_secret
        self.last_updatedTime = last_updatedTime
        self.last_transactions = self.order_datas(last_transactions)

        # 2 - Variables
        self.b_client = None
        self.b_balance = None
        self.u_assets = []
        self.u_symbols = []
        self.b_timestamps = []

        # 3 - Outputs
        self.u_balance = []
        self.u_trades_closed = []
        self.u_trades_open = []
        self.u_day_value = []
        self.u_transferts = []

        # 4 - Beginning (5 - 20 min)
        self.set_data()
    
    def set_data(self):
        self.__get_b_client()

        self.__get_b_balance()

        self.set_u_assets()

        self.set_u_balance()

        self.set_u_symbols()

        self.get_u_trades_closed()

        self.set_u_trades_open()

        self.__get_b_timestamps()

        self.set_u_withdraw_deposit_history()
        
        self.set_u_day_value()

        # sort
        self.u_trades_closed = self.order_datas(self.u_trades_closed)
        self.u_trades_open = self.order_datas(self.u_trades_open)
        self.u_day_value = self.order_datas(self.u_day_value)
        self.u_transferts = self.order_datas(self.u_transferts)

        # cas synchronisation
        i_stop = 0
        i = 0
        if self.last_updatedTime != '1498867200000':
            for trade in self.u_trades_closed:
                if i_stop == 0 and float(trade['timestamp']) > float(self.last_updatedTime):
                    i_stop = i
                i += 1
            self.u_trades_closed = self.u_trades_closed[i_stop:]
        

    def __get_b_client(self):
        print('1 - Getting Binance Client')
        self.b_client = Client(self.api_key, self.api_secret)

    def __get_b_balance(self):
        print('2 - Getting Binance User Acount')
        self.b_balance = self.b_client.get_account()

    def __get_b_day_balance(self, start = False, end = False):
        # get daily balance
        try:
            if start and end:
                b_day_balance = self.b_client.get_account_snapshot(type='SPOT', startTime=start, endTime=end)
            else:
                b_day_balance = self.b_client.get_account_snapshot(type='SPOT')
        except BinanceAPIException as e:
            print(e, 'Wait 30sec')
            time.sleep(30)
            b_day_balance = self.__get_b_day_balance(start, end)
        return b_day_balance


    def set_u_assets(self):
        print('3 - Getting assets usually used by user')
        # get assets already traded by the user
        b_day_balance = self.__get_b_day_balance()
        for balance in b_day_balance['snapshotVos'][0]['data']['balances']:
            self.u_assets.append(balance['asset'])

    def __get_b_price_now(self, symbol):
        return self.b_client.get_avg_price(symbol=symbol)['price']

    def set_u_balance(self):
        print('4 - Getting User Last Balance')
        # for each asset
        for balance in self.b_balance['balances']:
            quantity_locked = float(balance['locked'])
            quantity_free = float(balance['free'])
            # if quantity != 0
            if quantity_locked + quantity_free != 0:

                # get value in USDT
                if balance['asset'] in ('USDT', 'USD'):
                    value = quantity_locked + quantity_free
                else:
                    symbol = balance['asset'] + 'USDT'
                    try:
                        price = float(self.__get_b_price_now(symbol))
                    except BinanceAPIException:
                        btc_price = float(self.__get_b_price_now('BTCUSDT'))
                        try:
                            symbol = balance['asset'] + 'BTC'
                            price = float(self.__get_b_price_now(symbol))
                            price = price / btc_price
                        except BinanceAPIException as e:
                            price = 0
                            print(e, 'Cannot get price for', symbol)

                    value = (price * (quantity_locked + quantity_free))
                
                row = {'coin': balance['asset'], 'quantity_free': quantity_free, 'quantity_locked': quantity_locked, 'quantity_total': quantity_free + quantity_locked, 'value': value, 'updatedTime': self.b_balance['updateTime']}
                self.u_balance.append(row)

    def set_u_symbols(self):
        print('5 - Getting symbols traded by the User')
        symbols = []
        # get all symbols of the exchange
        infos = self.b_client.get_exchange_info()
        for b_symbols in infos['symbols']:
            if b_symbols['isSpotTradingAllowed'] == True:
                symbols.append(b_symbols['symbol'])
        # get all the possible symbols that the user could have trade
        for asset2 in self.u_assets:
            for asset1 in self.u_assets:
                symbol = asset1 + asset2
                if symbol in symbols:
                    row = {'symbol': symbol, 'baseAsset': asset1, 'quoteAsset': asset2}
                    self.u_symbols.append(row)

    def __get_b_trades(self, symbol, fromId = 1):
        try:
            trades = self.b_client.get_my_trades(symbol=symbol, limit=1000, fromId=fromId)
        except BinanceAPIException as e:
            print(e, 'Too much calls, wait for 1min please')
            time.sleep(60)
            trades = self.__get_b_trades(symbol, fromId)
        return trades
        
    def __get_b_candle_USDT(self, timestamp, asset, quantity):
        symbol = asset + 'USDT'
        startTime = timestamp
        endTime = timestamp + 60000
        try:
            price = self.b_client.get_klines(symbol=symbol, interval='1m', startTime=startTime, endTime=endTime, limit=1)
        except BinanceAPIException as e:
            btc_price = self.b_client.get_klines(symbol='BTCUSDT', interval='1m', startTime=startTime, endTime=endTime, limit=1)
            try:
                symbol = asset + 'BTC'
                price = self.b_client.get_klines(symbol=symbol, interval='1m', startTime=startTime, endTime=endTime, limit=1)
                if price != []:
                    price = [[[], float(price[0][1]) / float(btc_price[0][1])]]
            except BinanceAPIException as e:
                price = []
                print(e, 'Cannot get price')

        if price == []:
            price = 0
            print('No price for this symbol at this time', symbol, timestamp)
        else:
            price = float(price[0][1])
        return (float(quantity) * float(price))
    

    def __set_u_trades_closed(self, trades, symbol, too_much_trades):
        this_trades = []
        for trade in trades:
            # get base and quote asset associate to the symbol
            for u_symbol in self.u_symbols:
                if symbol == u_symbol['symbol']:
                    baseAsset = u_symbol['baseAsset']
                    quoteAsset = u_symbol['quoteAsset']
            # trade_type, received_currency, sent_currency, received_quantity, sent_quantity
            if trade['isBuyer'] == True:
                trade_type = 'BUY'
                received_currency = baseAsset
                sent_currency = quoteAsset
                received_quantity = float(trade['qty'])
                sent_quantity = float(trade['quoteQty'])
            else:
                trade_type = 'SELL'
                received_currency = quoteAsset
                sent_currency = baseAsset
                received_quantity = float(trade['quoteQty'])
                sent_quantity = float(trade['qty'])
            
            # trade and fee value in USDT
            if quoteAsset in ('USDT', 'USD'):
                trade_value = float(trade['price']) * float(trade['qty'])
            elif trade_type == 'BUY':
                trade_value = self.__get_b_candle_USDT(trade['time'], sent_currency, sent_quantity)
            elif trade_type == 'SELL':
                trade_value = self.__get_b_candle_USDT(trade['time'], received_currency, received_quantity)
            if trade['commissionAsset'] in ('USDT', 'USD'):
                fee_value = float(trade['commission'])
            else:
                fee_value = self.__get_b_candle_USDT(trade['time'], trade['commissionAsset'], float(trade['commission']))
            # set u_trades_closed
            row = {'timestamp': trade['time'], 'type': trade_type, 'symbol': symbol, 'received_currency': received_currency, 'received_quantity': received_quantity, 'sent_currency': sent_currency, 'sent_quantity': sent_quantity, 'fee_currency': trade['commissionAsset'], 'fee_quantity': float(trade['commission']), 'trade_value': trade_value, 'fee_value': fee_value, 'orderId': trade['orderId']}
            this_trades.append(row)
            self.u_trades_closed.append(row)

        if too_much_trades:
            print('It will take a longer time, too much trades for this symbol : ', symbol)
            fromId = this_trades[0]['orderId']
            trades = self.__get_b_trades(symbol, fromId)
            if len(trades) > 0 and len(trades) < 1000:
                self.__set_u_trades_closed(trades, symbol, False)
            elif len(trades) >= 1000 : 
                self.__set_u_trades_closed(trades, symbol, True)


    def get_u_trades_closed(self):
        print('6 - Getting User trades closed')
        for u_symbol in self.u_symbols:
            symbol = u_symbol['symbol']
            fromId = 1
            if self.last_updatedTime != '1498867200000':
                for transaction in self.last_transactions:
                    if symbol == transaction['symbol']:
                        fromId = transaction['orderId']
            trades = self.__get_b_trades(symbol, fromId)
            # max len for b_trades : 1000
            if len(trades) > 0 and len(trades) < 1000:
                # if symbol == 'BTCUSDT':
                #     self.__set_u_trades_closed(trades, symbol, True)
                # else:
                self.__set_u_trades_closed(trades, symbol, False)
            elif len(trades) >= 1000 : 
                self.__set_u_trades_closed(trades, symbol, True)

    def __get_b_trades_open(self):
        try:
            trades = self.b_client.get_open_orders()
        except BinanceAPIException as e:
            print(e, 'Too much calls, wait for 1min')
            time.sleep(60)
            trades = self.__get_b_trades_open()
        return trades

    def set_u_trades_open(self):
        print('7 - Getting User trades openned')
        trades = self.__get_b_trades_open()
        for trade in trades:
            row = {'timestamp': trade['time'], 'type': trade['side'], 'symbol': trade['symbol'], 'quantity': trade['origQty'], 'price': trade['price']}
            self.u_trades_open.append(row)        

    def __get_b_timestamps(self):
        print('8 - Getting period timestamp')
        endTime = time.time()*1000
        running = True
        while running:
            self.b_timestamps.append((round(endTime - 2592000000), round(endTime)))
            endTime -= 2592000000
            if endTime - 2592000000 < float(self.last_updatedTime):
                self.b_timestamps.append((round(float(self.last_updatedTime)), round(endTime)))
                running = False
        
    def set_u_day_value(self):
        print('12 - Getting User Wallet value evolution')
        running = True
        i = 0
        while running:
            start = str(self.b_timestamps[i][0])
            end = str(self.b_timestamps[i][1])
            b_day_balance = self.__get_b_day_balance(start, end)
            if b_day_balance['snapshotVos'] != []:
                for balance in b_day_balance['snapshotVos']:
                    row = {'timestamp': balance['updateTime'], 'wallet_value_BTC': float(balance['data']['totalAssetOfBtc']), 'wallet_value_USDT': self.__get_b_candle_USDT(balance['updateTime'], 'BTC', float(balance['data']['totalAssetOfBtc'])), 'balances': balance['data']['balances']}
                    self.u_day_value.append(row)
            else:
                running = False
            i += 1
            if i >= len(self.b_timestamps):
                running = False

    def order_datas(self, datas):
        datas = sorted(datas, key=lambda k: k['timestamp']) 
        return datas

    def set_u_withdraw_deposit_history(self):
        self.__get_u_withdraw()
        self.__get_u_deposit()
        self.u_transferts = self.order_datas(self.u_transferts)
        for i in range(0, len(self.u_transferts)) :
            if i == 0:
                if self.u_transferts[i]['type'] == 'DEPOSIT':
                    self.u_transferts[i]['deposit_withdraw_USDT'] = float(self.u_transferts[i]['transaction_value'])
                elif self.u_transferts[i]['type'] == 'WITHDRAW':
                    self.u_transferts[i]['deposit_withdraw_USDT'] = -1 * (float(self.u_transferts[i]['transaction_value']) + float(self.u_transferts[i - 1]['fee_value']))
            else:
                if self.u_transferts[i]['type'] == 'DEPOSIT':
                    self.u_transferts[i]['deposit_withdraw_USDT'] = float(self.u_transferts[i - 1]['deposit_withdraw_USDT']) + float(self.u_transferts[i]['transaction_value'])
                elif self.u_transferts[i]['type'] == 'WITHDRAW':
                    self.u_transferts[i]['deposit_withdraw_USDT'] = float(self.u_transferts[i - 1]['deposit_withdraw_USDT']) - float(self.u_transferts[i]['transaction_value']) - float(self.u_transferts[i]['fee_value'])

    def __get_u_withdraw(self):
        print('10 - Getting User Withdraws history')
        # get status (0:Email Sent,1:Cancelled 2:Awaiting Approval 3:Rejected 4:Processing 5:Failure 6:Completed)
        def email():
            return 'Email Sent'
        def cancelled():
            return 'Cancelled'
        def awaiting():
            return 'Awaiting Approval'
        def rejected():
            return 'Rejected'
        def processing():
            return 'Processing'
        def failure():
            return 'Failure'
        def completed():
            return 'Completed'
        options = {'0': email, '1': cancelled, '2': awaiting, '3': rejected, '4': processing, '5': failure, '6': completed}

        for i in range(0, len(self.b_timestamps)):
            start = str(self.b_timestamps[i][0])
            end = str(self.b_timestamps[i][1])
            withdraws = self.b_client.get_withdraw_history(startTime=start, endTime=end)
            if withdraws != []:
                for withdraw in withdraws:
                    date = datetime.strptime(withdraw['applyTime'], "%Y-%m-%d %H:%M:%S")
                    date = round(datetime.timestamp(date)*1000)
                    if withdraw['coin'] not in ('USD', 'USDT'):
                        transaction_value = self.__get_b_candle_USDT(date, withdraw['coin'], withdraw['amount'])
                        fee_value = self.__get_b_candle_USDT(date, withdraw['coin'], withdraw['transactionFee'])
                    else:
                        transaction_value = withdraw['amount']
                        fee_value = withdraw['transactionFee']
                    if 'network' in withdraw:
                        network = withdraw['network']
                    else:
                        network = ''
                    row = {'timestamp': date, 'type': 'WITHDRAW', 'coin': withdraw['coin'], 'quantity': withdraw['amount'], 'fees': withdraw['transactionFee'], 'transaction_value': transaction_value, 'fee_value' : fee_value, 'network': network, 'address': withdraw['address'], 'status': options[str(withdraw['status'])](), 'deposit_withdraw_USDT': 0}
                    self.u_transferts.append(row)

    def __get_u_deposit(self):
        print('11 - Getting User Deposits history')

        # get status (0:pending,6: credited but cannot withdraw, 1:success)
        def pending():
            return 'Pending'
        def cannot_withdraw():
            return 'Credited but cannot withdraw'
        def success():
            return 'Completed'
        options = {'0': pending, '1': success, '6': cannot_withdraw}

        for i in range(0, len(self.b_timestamps)):
            start = str(self.b_timestamps[i][0])
            end = str(self.b_timestamps[i][1])
            deposits = self.b_client.get_deposit_history(startTime=start, endTime=end)
            if deposits != []:
                for deposit in deposits:
                    amount = float(deposit['amount'])
                    if deposit['coin'] not in ('USD', 'USDT'):
                        transaction_value = self.__get_b_candle_USDT(deposit['insertTime'], deposit['coin'], amount)
                    else:
                        transaction_value = amount
                    row = {'timestamp': deposit['insertTime'], 'type': 'DEPOSIT', 'coin': deposit['coin'], 'quantity': amount, 'fees': 0, 'transaction_value': transaction_value, 'fee_value' : 0, 'network': deposit['network'], 'address': deposit['address'], 'status': options[str(deposit['status'])](), 'deposit_withdraw_USDT': 0}
                    self.u_transferts.append(row)