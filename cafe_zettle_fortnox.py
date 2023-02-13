import json

f = open("response.json")
data = json.load(f)
f.close()

test = {}

cafeDesc = "IR Caféverksamhet"
voucherSeries = "A"
year = 2023
vouchers  = []
for date, v in data["cafe"].items():
    test[date] = {}
    for itemName, item in v.items():
        if item["account"] in test[date]:
            test[date][item["account"]] += item["quantity"] * item["unit_price"]
        else:
            test[date][item["account"]] = item["quantity"] * item["unit_price"]
    vouchers.append(
        {
        "Voucher" : {
            "Description" : cafeDesc,
            "TransactionDate": date,
            "VoucherSeries" : voucherSeries,
            "Year" : year,
            "VoucherRows" : [
                {
                    "Account" : account,
                    "Credit" : amount/100
                 } for account, amount in test[date].items()
            ]
        }
        }
    )



print(vouchers)
