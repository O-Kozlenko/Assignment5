deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08, #8% річних
    "is active": True
}
suma = deposit_account["balance"]*(1+deposit_account["interest_rate"])
deposit_account["balance"]=suma
deposit_account["last_update_type"]= "interest accrual"
deposit_account["is active"] = False
print(deposit_account)