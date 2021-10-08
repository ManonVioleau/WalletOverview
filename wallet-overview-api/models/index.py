from config.db import meta, engine
from models.users import users
from models.balances import balances
from models.platforms import platforms
from models.trades_closed import trades_closed
from models.trades_open import trades_open
from models.transferts import transferts
from models.wallet import wallets
from models.wallets_evolutions import wallets_evolutions
from models.means_trades import means_trades
from models.transferts_ordered import transferts_ordered

meta.create_all(engine)