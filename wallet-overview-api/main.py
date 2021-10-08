from fastapi import FastAPI
from routes.index import user, wallet, platform, synchronisation, balance, trade_closed, trade_open, transfert, wallet_evolution, mean_trade, transfert_ordered
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    # allow_headers=["*"],
)
app.include_router(user)
app.include_router(platform)
app.include_router(wallet)
app.include_router(synchronisation)
app.include_router(balance)
app.include_router(trade_closed)
app.include_router(trade_open)
app.include_router(transfert)
app.include_router(wallet_evolution)
app.include_router(mean_trade)
app.include_router(transfert_ordered)