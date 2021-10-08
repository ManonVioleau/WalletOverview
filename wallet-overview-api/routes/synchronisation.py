from fastapi import APIRouter
import json 
import time
from fastapi.encoders import jsonable_encoder
from sqlalchemy.sql.expression import delete
from config.db import conn
from models.index import wallets, balances
from schemas.index import Synchronisation, Balance, Trade_closed, Trade_open, Transfert, Wallet_evolution, Mean_trade, Transfert_ordered
from datetime import datetime
from platforms.Binance import User_Binance
from routes.balance import write_data as post_balance, delete_data_user_platform_id as delete_balance
from routes.trade_closed import write_data as post_trades_closed, delete_data_user_platform_id as delete_trades_closed
from routes.trade_open import write_data as post_trades_open, delete_data_user_platform_id as delete_trades_open
from routes.transfert import write_data as post_transferts, delete_data_user_platform_id as delete_transferts
from routes.transfert_ordered import write_data as post_transferts_ordered, delete_data_user_platform_id as delete_transferts_ordered
from routes.wallet_evolution import write_data as post_wallet_evolution, delete_data_user_platform_id as delete_wallet_evolution
from routes.mean_trade import write_data as post_mean_trade, delete_data_user_platform_id as delete_mean_trade

synchronisation = APIRouter()

@synchronisation.post("/synchronisation/")
async def get_data(synchronisation: Synchronisation):

    start = time.time()
    # get wallet associate
    wallet = conn.execute(wallets.select().where(wallets.c.user_id == synchronisation.user_id and wallets.c.platform_id == synchronisation.platform_id)).fetchone()

    # construction of the object to the api calls (binance)
    object = User_Binance(wallet.api_key, wallet.api_secret)

    # balances
    get_balances = getattr(object,"u_balance")
    delete = await delete_balance(synchronisation.user_id, synchronisation.platform_id)
    for get_balance in get_balances:
        balance = Balance(
            user_id= synchronisation.user_id,
            platform_id= synchronisation.platform_id,
            coin= get_balance['coin'],
            quantity_free= get_balance['quantity_free'],
            quantity_locked= get_balance['quantity_locked'],
            quantity_total= get_balance['quantity_total'],
            value= get_balance['value']
        )
        balance = await post_balance(balance)
    
    # trades_closed
    get_trades_closed = getattr(object,"u_trades_closed")
    delete = await delete_trades_closed(synchronisation.user_id, synchronisation.platform_id)
    for get_trade_closed in get_trades_closed:
        trades_closed = Trade_closed(
            user_id= synchronisation.user_id,
            platform_id= synchronisation.platform_id,
            date = datetime.fromtimestamp(float(get_trade_closed['timestamp'])/1000),
            timestamp = get_trade_closed['timestamp'],
            type = get_trade_closed['type'],
            symbol = get_trade_closed['symbol'],
            received_currency = get_trade_closed['received_currency'],
            received_quantity = get_trade_closed['received_quantity'],
            sent_currency = get_trade_closed['sent_currency'],
            sent_quantity = get_trade_closed['sent_quantity'],
            fee_currency = get_trade_closed['fee_currency'],
            fee_quantity = get_trade_closed['fee_quantity'],
            trade_value = get_trade_closed['trade_value'],
            fee_value = get_trade_closed['fee_value'],
            orderId = get_trade_closed['orderId']
        )
        trades_closed = await post_trades_closed(trades_closed)
    
    # trades_open
    get_trades_open = getattr(object,"u_trades_open")
    delete = await delete_trades_open(synchronisation.user_id, synchronisation.platform_id)
    for get_trade_open in get_trades_open:
        trades_open = Trade_open(
            user_id= synchronisation.user_id,
            platform_id= synchronisation.platform_id,
            date = datetime.fromtimestamp(float(get_trade_open['timestamp'])/1000),
            timestamp = get_trade_open['timestamp'],
            type = get_trade_open['type'],
            symbol = get_trade_open['symbol'],
            quantity = get_trade_open['quantity'],
            price = get_trade_open['price']
        )
        trades_open = await post_trades_open(trades_open)

    # transferts
    get_transferts = getattr(object,"u_transferts")
    delete = await delete_transferts(synchronisation.user_id, synchronisation.platform_id)
    for get_transfert in get_transferts:
        transferts = Transfert(
            user_id= synchronisation.user_id,
            platform_id= synchronisation.platform_id,
            date = datetime.fromtimestamp(float(get_transfert['timestamp'])/1000),
            timestamp = get_transfert['timestamp'],
            type = get_transfert['type'],
            coin = get_transfert['coin'],
            quantity = get_transfert['quantity'],
            fees = get_transfert['fees'],
            transfert_value = get_transfert['transaction_value'],
            fee_value = get_transfert['fee_value'],
            network = get_transfert['network'],
            address = get_transfert['address'],
            status = get_transfert['status'],
            dep_with_value = get_transfert['deposit_withdraw_USDT']
        )
        transferts = await post_transferts(transferts)

    # wallets_evolutions
    get_wallets_evolutions = getattr(object,"u_day_value")
    delete = await delete_wallet_evolution(synchronisation.user_id, synchronisation.platform_id)
    for get_wallet_evolution in get_wallets_evolutions:
        wallets_evolutions = Wallet_evolution(
            user_id= synchronisation.user_id,
            platform_id= synchronisation.platform_id,
            date = datetime.fromtimestamp(float(get_wallet_evolution['timestamp'])/1000),
            timestamp = get_wallet_evolution['timestamp'],
            wallet_value_BTC = get_wallet_evolution['wallet_value_BTC'],
            wallet_value_USDT = get_wallet_evolution['wallet_value_USDT']
        )
        wallets_evolutions = await post_wallet_evolution(wallets_evolutions)

    # transferts_ordered
    transferts = get_transferts
    walletevolution = get_wallets_evolutions
    delete = await delete_transferts_ordered(synchronisation.user_id, synchronisation.platform_id)
    new_transfert = []
    
    for wallet in walletevolution:
        for i in range(0, len(transferts)):
            if transferts[i]['timestamp'] > wallet['timestamp']:
                date = datetime.fromtimestamp(float(wallet['timestamp'])/1000)
                timestamp = wallet['timestamp']
                value = transferts[i - 1]['deposit_withdraw_USDT']
                row = {'date': date, 'timestamp': timestamp, 'value': value}
                new_transfert.append(row)
                break
            elif i == len(transferts) - 1:
                date = datetime.fromtimestamp(float(wallet['timestamp'])/1000)
                timestamp = wallet['timestamp']
                value = transferts[i]['deposit_withdraw_USDT']
                row = {'date': date, 'timestamp': timestamp, 'value': value}
                new_transfert.append(row)

    for transfert in new_transfert:
        transferts_order = Transfert_ordered(
            user_id= synchronisation.user_id,
            platform_id= synchronisation.platform_id,
            date = transfert['date'],
            timestamp = transfert['timestamp'],
            value = transfert['value']
        )
        transferts_order = await post_transferts_ordered(transferts_order)

    # means_trades
    delete = await delete_mean_trade(synchronisation.user_id, synchronisation.platform_id)
    means_trades = {}
    assets = []
    for get_trade_closed in get_trades_closed:
        type = get_trade_closed['type']
        received_currency = get_trade_closed['received_currency']
        received_quantity = get_trade_closed['received_quantity']
        sent_currency = get_trade_closed['sent_currency']
        sent_quantity = get_trade_closed['sent_quantity']
        trade_value = get_trade_closed['trade_value']

        if type == 'BUY' and received_currency not in ('USD', 'USDT'):
            if received_currency not in assets:
                assets.append(received_currency)
            if f"{received_currency}_buy_total_value" in means_trades:
                means_trades[f"{received_currency}_buy_total_value"] += trade_value
            else:
                means_trades[f"{received_currency}_buy_total_value"] = trade_value
            if f"{received_currency}_buy_total_quantity" in means_trades:
                means_trades[f"{received_currency}_buy_total_quantity"] += received_quantity
            else:
                means_trades[f"{received_currency}_buy_total_quantity"] = received_quantity

        elif type == 'SELL' and sent_currency not in ('USD', 'USDT'):
            if sent_currency not in assets:
                assets.append(sent_currency)
            if f"{sent_currency}_sell_total_value" in means_trades:
                means_trades[f"{sent_currency}_sell_total_value"] += trade_value
            else:
                means_trades[f"{sent_currency}_sell_total_value"] = trade_value
            if f"{sent_currency}_sell_total_quantity" in means_trades:
                means_trades[f"{sent_currency}_sell_total_quantity"] += sent_quantity
            else:
                means_trades[f"{sent_currency}_sell_total_quantity"] = sent_quantity

    datas = []

    for asset in assets:
        buy_total_value = 0
        buy_total_quantity = 0
        sell_total_value = 0
        sell_total_quantity = 0
        mean_buy = 0
        mean_sell = 0
        buy_minus_sell = 0
        if f"{asset}_buy_total_value" in means_trades:
            buy_total_value = means_trades[f"{asset}_buy_total_value"]
        if f"{asset}_sell_total_value" in means_trades:
            sell_total_value = means_trades[f"{asset}_sell_total_value"]
        if f"{asset}_buy_total_quantity" in means_trades:
            buy_total_quantity = means_trades[f"{asset}_buy_total_quantity"]
        if f"{asset}_sell_total_quantity" in means_trades:
            sell_total_quantity = means_trades[f"{asset}_sell_total_quantity"]

        if buy_total_value and buy_total_quantity:
            mean_buy = buy_total_value / buy_total_quantity
        if sell_total_value and sell_total_quantity:
            mean_sell = sell_total_value / sell_total_quantity
        if buy_total_value and sell_total_value:
            buy_minus_sell = buy_total_value - sell_total_value

        row = {"coin": asset, 'mean_buy': mean_buy, 'mean_sell': mean_sell, 'buy_minus_sell': buy_minus_sell, 'percent_gain_loss': 0}
        datas.append(row)

    for get_mean_trade in datas:
        means_trades = Mean_trade(
            user_id= synchronisation.user_id,
            platform_id= synchronisation.platform_id,
            coin = get_mean_trade['coin'],
            mean_buy = get_mean_trade['mean_buy'],
            mean_sell = get_mean_trade['mean_sell'],
            buy_minus_sell = get_mean_trade['buy_minus_sell'],
            percent_gain_loss = get_mean_trade['percent_gain_loss']
        )
        means_trades = await post_mean_trade(means_trades)

    end = time.time()
    print(f'time : {round(float(format(end - start))/60)}min {round((float(format(end - start))/60- round(float(format(end - start))/60)) * 60)}sec')

    return 'ok'